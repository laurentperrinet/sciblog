"""Build a fully client-side search index with Pagefind.

Pagefind (https://pagefind.app/) indexes the *rendered* HTML of the site and
emits a small static bundle -- a WebAssembly search engine plus chunked,
pre-ranked index files -- that runs entirely in the visitor's browser: no
server, no crawler, no third-party API, no key.  That is exactly what a static
Nikola site hosted on GitHub Pages needs.

The plugin is a ``LateTask``, so it runs once every other Nikola task has
written its output into ``OUTPUT_FOLDER``: the HTML it indexes is the HTML that
will be published.  It then calls the ``pagefind`` binary, looked up in this
order:

1. ``PAGEFIND_BINARY`` from :file:`conf.py` (explicit path);
2. :envvar:`PAGEFIND_BIN` from the environment (handy for CI);
3. :file:`node_modules/.bin/pagefind`, i.e. after ``npm install`` in the site root;
4. ``pagefind`` on :envvar:`PATH`;
5. a cached download in ``CACHE_FOLDER/pagefind/<version>/``, enabled by
   ``PAGEFIND_DOWNLOAD``.  Pagefind ships one self-contained binary per
   platform, so this last step needs no Node.js -- which is what lets the
   Docker-based ``getnikola/nikola-action`` CI job build the index unmodified.

Two constraints drive the implementation:

* **Never break a build or a deployment.**  If no binary is found, or Pagefind
  fails, the task logs a warning and succeeds, keeping whatever index already
  exists.  Missing search is a degraded site; a failed deployment is an outage.
  Set ``PAGEFIND_STRICT = True`` to turn failures into build errors instead.
* **Stay cheap.**  Freshness uses ``stat()`` fingerprints (size and mtime) plus
  an options hash rather than reading hundreds of megabytes of notebook HTML;
  Pagefind keeps its own incremental cache for unchanged pages, so rebuilding
  an unchanged site costs one ``stat`` pass.

Every setting is documented in the ``PAGEFIND_*`` block of :file:`conf.py`.
"""

from __future__ import annotations

import functools
import glob as glob_module
import hashlib
import json
import os
import platform
import shutil
import subprocess
import tarfile
import tempfile
import urllib.request

from nikola import utils
from nikola.plugin_categories import LateTask

#: Keep in sync with the ``pagefind`` dev dependency in :file:`package.json`
#: and with ``PAGEFIND_VERSION`` in :file:`conf.py`.
DEFAULT_PAGEFIND_VERSION = "1.5.2"

#: Which rendered pages to index, as a single Pagefind (globset) pattern
#: relative to ``OUTPUT_FOLDER``.  Notebook *posts* and Markdown *pages* are
#: the content; the theme taxonomy pages are navigable by tag and would only
#: add duplicate hits.
DEFAULT_PAGEFIND_GLOB = "{posts,pages}/*.html"

#: Release asset suffix per platform (``pagefind-v<version>-<suffix>.tar.gz``).
PLATFORM_SUFFIXES = {
    ("Darwin", "arm64"): "aarch64-apple-darwin",
    ("Darwin", "x86_64"): "x86_64-apple-darwin",
    ("Linux", "x86_64"): "x86_64-unknown-linux-musl",
    ("Linux", "amd64"): "x86_64-unknown-linux-musl",
    ("Linux", "aarch64"): "aarch64-unknown-linux-musl",
    ("Linux", "arm64"): "aarch64-unknown-linux-musl",
}

#: Tasks whose output is our input.  As a ``LateTask`` we already run last, but
#: declaring them keeps the task correct when built in isolation.
RENDER_TASKS = (
    "render_posts",
    "render_pages",
    "render_sources",
    "render_listings",
    "copy_files",
    "copy_assets",
)

#: Fallback exclusions when ``PAGEFIND_EXCLUDE_SELECTORS`` is left as ``None``.
#: They drop the theme chrome and, above all, the notebook machinery: Jupyter
#: source prompts and stdout/stderr dumps would otherwise dominate the index
#: (this library holds ~19 MB of visible text, most of it execution logs).
DEFAULT_EXCLUDE_SELECTORS = (
    # Theme chrome: navigation, teasers, tag clouds, the search box itself.
    "nav",
    "header",
    "footer",
    "aside",
    ".navbar",
    ".blog-header",
    ".post-list",
    ".pager",
    ".pagination",
    "#search",
    ".pagefind-ui__suppress-pagefind-ui",
    # Notebook machinery: code cells, input prompts, and execution logs.
    "pre",
    "code",
    ".highlight",
    ".prompt",
    ".output",
    ".output_wrapper",
    ".output_area",
    ".output_subarea",
    ".output_text",
    ".stderr",
    ".jp-RenderedText",
    ".jp-InputArea",
)


class PagefindSearch(LateTask):
    """Generate the Pagefind search bundle inside ``OUTPUT_FOLDER``."""

    name = "pagefind_index"

    # ------------------------------------------------------------------ setup

    def set_site(self, site):
        """Register the defaults this plugin contributes to :file:`conf.py`."""
        super().set_site(site)
        defaults = {
            "PAGEFIND_ENABLED": True,
            "PAGEFIND_STRICT": False,
            "PAGEFIND_BINARY": "",
            "PAGEFIND_VERSION": DEFAULT_PAGEFIND_VERSION,
            "PAGEFIND_DOWNLOAD": True,
            "PAGEFIND_OUTPUT_DIR": "pagefind",
            "PAGEFIND_BASE_URL": "",
            "PAGEFIND_GLOB": DEFAULT_PAGEFIND_GLOB,
            "PAGEFIND_EXCLUDE_SELECTORS": None,
            "PAGEFIND_EXTRA_ARGS": (),
            "PAGEFIND_LOG_LEVEL": "info",
        }
        for key, value in defaults.items():
            # ``nikola.config.Config`` raises ``ConfigNotFound`` for unknown
            # keys, so seed the settings that :file:`conf.py` does not define.
            try:
                site.config[key]
            except Exception:
                site.config[key] = value
        return None

    # ------------------------------------------------------------------ tasks

    def gen_tasks(self):
        """Yield the doit task that builds the Pagefind index."""
        config = self.site.config
        output_folder = config["OUTPUT_FOLDER"]
        out_dir = (config["PAGEFIND_OUTPUT_DIR"] or "pagefind").strip("/")
        index_dir = os.path.join(output_folder, out_dir)
        entry_target = os.path.join(index_dir, "pagefind-entry.json")

        # Snapshot the options that change the produced bundle; embedding them
        # in the fingerprint makes an option edit invalidate the index.
        kw = {
            "version": config["PAGEFIND_VERSION"],
            "output_dir": out_dir,
            "base_url": config["PAGEFIND_BASE_URL"],
            "glob": config["PAGEFIND_GLOB"] or DEFAULT_PAGEFIND_GLOB,
            "exclude": list(config["PAGEFIND_EXCLUDE_SELECTORS"] or DEFAULT_EXCLUDE_SELECTORS),
            "extra_args": list(config["PAGEFIND_EXTRA_ARGS"]),
            "log_level": config["PAGEFIND_LOG_LEVEL"],
        }

        yield self.group_task()

        if not config["PAGEFIND_ENABLED"]:
            self.logger.info("Pagefind search is disabled (PAGEFIND_ENABLED = False).")
            return

        html_files = _html_files(output_folder, kw["glob"])
        if not html_files:
            self.logger.warning(
                "Pagefind: no HTML found under %r with PAGEFIND_GLOB=%r; "
                "search index skipped.", output_folder, kw["glob"],
            )
            return

        task = {
            "basename": self.name,
            "name": "index",
            "targets": [entry_target],
            "actions": [(self._build_index, (html_files, output_folder, index_dir, kw))],
            "clean": [(_clean_index, (index_dir,))],
            "task_dep": list(RENDER_TASKS),
            # doit calls a plain callable with *no* arguments unless its
            # parameters are literally named ``task``/``values``, so bind
            # everything up front rather than declaring positional ones.
            "uptodate": [functools.partial(
                self._is_uptodate, html_files, entry_target, kw
            )],
            "file_dep": [],
        }
        yield utils.apply_filters(task, config["FILTERS"])

    # -------------------------------------------------------------- discovery

    def _pagefind_binary(self, kw):
        """Locate (or download) the ``pagefind`` executable; ``None`` on failure."""
        config = self.site.config
        candidates = []
        explicit = config["PAGEFIND_BINARY"] or os.environ.get("PAGEFIND_BIN", "")
        if explicit:
            candidates.append(os.path.expanduser(explicit))
        root = config.get("ROOT") or os.getcwd()
        candidates.append(os.path.join(root, "node_modules", ".bin", "pagefind"))
        on_path = shutil.which("pagefind")
        if on_path:
            candidates.append(on_path)
        for candidate in candidates:
            if candidate and os.path.isfile(candidate) and os.access(candidate, os.X_OK):
                return candidate
        if config["PAGEFIND_DOWNLOAD"]:
            return self._download_binary(kw)
        return None

    def _download_binary(self, kw):
        """Download the pinned Pagefind release binary into the build cache.

        The archive is verified against the SHA-256 published in the same
        GitHub release and installed atomically, so an interrupted download can
        never leave a half-written binary behind.
        """
        version = kw["version"]
        suffix = PLATFORM_SUFFIXES.get((platform.system(), platform.machine()))
        if suffix is None:
            self.logger.warning(
                "Pagefind: no prebuilt binary for %s/%s. Run 'npm install' and "
                "set PAGEFIND_BINARY, or install Pagefind on PATH. Search skipped.",
                platform.system(), platform.machine(),
            )
            return None
        cache_root = os.path.join(self.site.config["CACHE_FOLDER"], "pagefind", version, suffix)
        binary = os.path.join(cache_root, "pagefind")
        if os.path.isfile(binary) and os.access(binary, os.X_OK):
            return binary

        asset = "pagefind-v{0}-{1}.tar.gz".format(version, suffix)
        base = "https://github.com/Pagefind/pagefind/releases/download/v{0}".format(version)
        try:
            os.makedirs(cache_root, exist_ok=True)
        except OSError as exc:
            self.logger.warning("Pagefind: cannot write %s (%s).", cache_root, exc)
            return None

        tmpdir = tempfile.mkdtemp(prefix="pagefind-", dir=cache_root)
        try:
            archive = os.path.join(tmpdir, asset)
            self.logger.info("Pagefind: downloading {0}/{1} ...".format(base, asset))
            urllib.request.urlretrieve("{0}/{1}".format(base, asset), archive)
            with urllib.request.urlopen("{0}/{1}.sha256".format(base, asset), timeout=60) as response:
                expected = response.read().decode("utf-8").split()[0].lower()
            actual = _sha256_file(archive)
            if actual != expected:
                raise RuntimeError(
                    "checksum mismatch for {0} (expected {1}, got {2})".format(asset, expected, actual)
                )
            with tarfile.open(archive, "r:gz") as tar:
                _extract_binary(tar, tmpdir)
            staged = os.path.join(tmpdir, "pagefind")
            if not os.path.isfile(staged):
                raise RuntimeError("archive {0} contains no 'pagefind' binary".format(asset))
            os.chmod(staged, 0o755)
            if os.path.exists(binary):
                os.remove(binary)
            shutil.move(staged, binary)
            return binary
        except Exception as exc:  # noqa: BLE001 - fail soft is the contract
            self.logger.warning(
                "Pagefind: could not download the pinned binary (%s). Run "
                "'npm install' or set PAGEFIND_BINARY. Search skipped.", exc,
            )
            return binary if os.path.isfile(binary) else None
        finally:
            shutil.rmtree(tmpdir, ignore_errors=True)

    # -------------------------------------------------------------------- run

    def _build_index(self, html_files, output_folder, index_dir, kw):
        """Run the Pagefind CLI over the rendered site."""
        binary = self._pagefind_binary(kw)
        if binary is None:
            return self._degraded(
                index_dir,
                "Pagefind binary not found (checked PAGEFIND_BINARY/PAGEFIND_BIN, "
                "node_modules/.bin/pagefind, PATH, and the release download)",
            )

        # ``--output-subdir`` is relative to the site (``--output-path`` would
        # be relative to the current directory, which is not where Nikola runs).
        cmd = [
            binary,
            "--site", output_folder,
            "--output-subdir", kw["output_dir"],
            "--glob", kw["glob"],
        ]
        if kw["exclude"]:
            # The CLI takes one comma-separated string, not a repeated flag.
            cmd += ["--exclude-selectors", ",".join(kw["exclude"])]
        cmd.extend(kw["extra_args"])
        log_level = (kw["log_level"] or "info").lower()
        verbosity = {"verbose": "-v", "debug": "-v", "quiet": "-q",
                     "silent": "--silent"}
        if log_level in verbosity:
            cmd.append(verbosity[log_level])

        self.logger.info(
            "Pagefind: indexing {0} HTML files from {1}/ into {2}/ ...".format(
                len(html_files), output_folder, kw["output_dir"]
            )
        )
        try:
            proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
        except OSError as exc:
            return self._degraded(index_dir, "could not run {0!r}: {1}".format(binary, exc))
        if proc.returncode != 0:
            detail = (proc.stderr or proc.stdout or "").strip().replace(os.linesep, " ")
            return self._degraded(
                index_dir, "Pagefind exited with {0}: {1}".format(proc.returncode, detail[:2000])
            )

        stdout = (proc.stdout or "").strip().replace(os.linesep, " ")
        if stdout:
            self.logger.info("Pagefind: %s", stdout)
        stale = _prune_stale_meta(index_dir)
        if stale:
            self.logger.info(
                "Pagefind: removed %d stale bundle file(s): %s",
                len(stale), ", ".join(stale),
            )
        _store_signature(self.site.config["CACHE_FOLDER"], html_files, kw)
        return True

    def _degraded(self, index_dir, reason):
        """Warn (or raise) and leave a placeholder so the search page copes."""
        if self.site.config["PAGEFIND_STRICT"]:
            raise RuntimeError(reason)
        self.logger.warning("%s. Search index left unchanged.", reason)
        _write_placeholder_index(index_dir)
        return True

    # -------------------------------------------------------------- freshness

    def _is_uptodate(self, html_files, entry_target, kw):
        """True when the index is present and nothing it depends on changed."""
        if not os.path.isfile(entry_target):
            return False
        if os.path.basename(entry_target) and _is_placeholder(entry_target):
            return False
        stored = _load_signature(self.site.config["CACHE_FOLDER"])
        return stored == _signature(html_files, kw)


# ------------------------------------------------------------------- helpers


def _html_files(output_folder, pattern):
    """Return the sorted list of rendered HTML files matching *pattern*.

    Pagefind globs accept ``{a,b}`` alternations, which :mod:`glob` does not,
    so the braces are expanded here to keep a single source of truth.
    """
    found = set()
    for expanded in _expand_braces(pattern):
        for path in glob_module.glob(os.path.join(output_folder, expanded)):
            if os.path.isfile(path):
                found.add(path)
    return sorted(found)


def _expand_braces(pattern):
    """Yield one pattern per combination of the ``{a,b}`` groups in *pattern*."""
    start = pattern.find("{")
    end = pattern.find("}", start + 1)
    if start < 0 or end < 0:
        yield pattern
        return
    for choice in pattern[start + 1:end].split(","):
        for rest in _expand_braces(pattern[:start] + choice + pattern[end + 1:]):
            yield rest


def _glob(pattern):
    """Glob that tolerates absent optional Nikola output folders."""
    return glob_module.glob(pattern)


def _sha256_file(path):
    """Hex SHA-256 digest of *path*, streamed (release archives are ~40 MB)."""
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _extract_binary(tar, dest):
    """Extract only the ``pagefind`` executable from a release archive."""
    for member in tar.getmembers():
        if os.path.basename(member.name) != "pagefind" or not member.isfile():
            continue
        source = tar.extractfile(member)
        if source is None:  # pragma: no cover - defensive
            continue
        with open(os.path.join(dest, "pagefind"), "wb") as out:
            shutil.copyfileobj(source, out)
        return


def _write_placeholder_index(index_dir):
    """Create a minimal entry file so the search page can detect 'no index'."""
    os.makedirs(index_dir, exist_ok=True)
    placeholder = os.path.join(index_dir, "pagefind-entry.json")
    if os.path.isfile(placeholder) and not _is_placeholder(placeholder):
        return
    with open(placeholder, "w", encoding="utf-8") as fh:
        json.dump({"version": "0.0.0-placeholder", "sites": {}}, fh)


def _is_placeholder(entry_path):
    """True for the marker written when indexing was unavailable."""
    try:
        with open(entry_path, encoding="utf-8") as fh:
            return "placeholder" in json.load(fh).get("version", "")
    except (OSError, ValueError):
        return True


def _prune_stale_meta(index_dir):
    """Delete ``*.pf_meta`` bundles no longer referenced by the index.

    Pagefind reuses content-hashed names for its language metadata but never
    removes the previous ones, so repeated builds would accumulate orphans in
    ``docs/pagefind/`` -- files that get committed and published for nothing.
    Only the names listed in :file:`pagefind-entry.json` are kept.

    Returns:
        The sorted names of the files that were removed.
    """
    entry_path = os.path.join(index_dir, "pagefind-entry.json")
    try:
        with open(entry_path, encoding="utf-8") as fh:
            entry = json.load(fh)
    except (OSError, ValueError):
        return []
    live = {
        "pagefind.{0}.pf_meta".format(info.get("hash"))
        for info in (entry.get("languages") or {}).values()
        if info.get("hash")
    }
    removed = []
    for name in sorted(os.listdir(index_dir)):
        if not name.endswith(".pf_meta") or name in live:
            continue
        try:
            os.remove(os.path.join(index_dir, name))
        except OSError:
            continue
        removed.append(name)
    return removed


def _clean_index(index_dir):
    """Remove the generated index bundle (``nikola clean``)."""
    if os.path.isdir(index_dir):
        shutil.rmtree(index_dir)
    return True


def _signature(html_files, kw):
    """Cheap fingerprint of the indexed content plus the effective options.

    The HTML is deliberately *not* hashed: some notebook pages here are tens of
    megabytes, and Pagefind keeps its own per-file cache, so a size-and-mtime
    fingerprint is enough to decide whether the CLI must run again.
    """
    digest = hashlib.sha256()
    digest.update(json.dumps(kw, sort_keys=True, default=str).encode("utf-8"))
    for path in html_files:
        try:
            stat = os.stat(path)
            stamp = "{0}\0{1}\0{2}\n".format(path, stat.st_size, stat.st_mtime_ns)
        except OSError:  # pragma: no cover - file vanished mid-build
            stamp = "{0}\0missing\n".format(path)
        digest.update(stamp.encode("utf-8"))
    return digest.hexdigest()


def _signature_path(cache_folder):
    return os.path.join(cache_folder, "pagefind", "signature.json")


def _store_signature(cache_folder, html_files, kw):
    """Persist the fingerprint of the content the index was built from."""
    path = _signature_path(cache_folder)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    payload = {"signature": _signature(html_files, kw), "files": len(html_files)}
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, sort_keys=True)
    os.replace(tmp, path)


def _load_signature(cache_folder):
    """Previously stored fingerprint, or ``None`` when unknown."""
    try:
        with open(_signature_path(cache_folder), encoding="utf-8") as fh:
            return json.load(fh).get("signature")
    except (OSError, ValueError):
        return None
