# AGENTS.md — Scientific Blog (Nikola)

When using opencode, limit the usage of agents only for language editing (improving the clarity, grammar, and phrasing of drafted text) and for limited technical assistance with code development. The tool should not be used for generating research ideas, formulating research questions or hypotheses, designing the methodology, conducting or interpreting data analysis, or performing mathematical derivations or calculations. All intellectual contributions, analytical work, and mathematical reasoning in this website are my own. I have reviewed all AI-assisted content and assume full responsibility for the accuracy and integrity of the entire work.

## Essential Commands

```bash
# Build the site
make build          # or: nikola build

# Serve locally (opens browser)
make serve          # or: nikola serve

# Clean build artifacts
make clean          # or: nikola clean

# Update dependencies
make update         # or: pip install -U -r requirements.txt

# Verify links/files in generated site
nikola check -l

# Create a new post (two-file format with metadata)
nikola new_post -f ipynb -2 -t "My Title" --tags="tag1, tag2"

# Deploy (handled by CI on push; manual:
nikola github_deploy   # or: git add docs/* && git commit -am 'updating site' && git push)
```

## Project Architecture

```
.
├── conf.py              # Nikola configuration (1450 lines)
├── posts/               # Source posts (~441 files): .md, .ipynb, .html
│   ├── *.ipynb          # Notebook content
│   └── *.meta           # Metadata: title, slug, date, tags, etc.
├── files/               # Static assets (images, videos, PDFs, notebooks)
├── listings/            # Code listing import scripts
├── plugins/             # Custom plugins (rest_html5, less, upgrade_metadata_v8)
├── docs/                # OUTPUT FOLDER — deployed to GitHub Pages
├── cache/               # Build cache (gitignored)
├── .venv/               # Python virtual environment (activate before nikola)
├── Makefile             # Simple command wrapper: build, serve, clean, update
└── requirements.txt     # Python dependencies: nikola, jupyterlab, etc.
```

Key: `posts/` = source; `docs/posts/` = generated output; edit only `posts/`.

## Content Conventions

### ISO8601 Naming
- Post filenames use `YYYY-MM-DD-<slug>` format
- Dates in metadata use `YYYY-MM-DD HH:MM:SS` (e.g., `2026-07-31 11:33:46 UTC+01:00`)
- Generated via `datetime.datetime.now().date().isoformat()`

### Two-File Post Format
- Created with `nikola new_post -f ipynb -2`
- Generates `posts/2025-06-09-title.ipynb` + `posts/2025-06-09-title.meta`
- Meta file contains: `.. title:`, `.. slug:`, `.. date:`, `.. tags:`, `.. link:`, `.. description:`, `.. type:`

### Scientific Tags (curated list)
```
python, blog, psychophysics, behavior, motionclouds, motion, saccades,
vision, retina, math, bicv, SLIP, Matching Pursuit, Motion Particles,
holoviews, pytorch, deep-learning, machine-learning, moviepy,
motionclouds, motion, saccades, Free Energy, learning
```
- Set with `--tags="tag1, tag2"` or in meta file
- Used for organization and filtering

### Teaser Marker
- Insert `<!-- TEASER_END -->` in notebooks to split index teasers from full content
- Also present in other posts in other formats (e.g., Markdown, reStructuredText).

### Asset Referencing
- Images/video from posts referenced as `../files/<filename>` (relative to output/)
- E.g., `![Teaser image](../files/2026-07-31-pale-blue-dots.svg)`

### Math Notation
- MathJax/KaTeX configured for `$...$` (inline) and `$$...$$` (display)
- Used extensively in scientific posts for equations

## Configuration Highlights (conf.py)

| Setting | Value | Notes |
|---|---|---|
| `OUTPUT_FOLDER` | `'docs'` | GitHub Pages serves from `/docs` |
| `THEME` | `'bootblog4'` | Bootstrap 4-based theme |
| `POSTS` | `('posts/*.md', 'posts/*.md', 'post.tmpl'), ('posts/*.ipynb', 'posts', 'post.tmpl'),` | Supports .md and .ipynb |
| `INDEX_TEASERS` | `True` | Teasers on index pages |
| `INDEX_DISPLAY_POST_COUNT` | `200` | Many posts per page |
| `FUTURE_IS_NOW` | `True` | Publish future-dated posts immediately |
| `DEPLOY_FUTURE` | `True` | Deploy future posts |
| `PRETTY_URLS` | `False` | URLs use `.html` extension |
| `TIMEZONE` | `'Europe/Paris'` | |
| `MATHJAX_CONFIG` | set | KaTeX auto-render enabled |
| `USE_TAG_METADATA` | `False` | Legacy tags (draft, private, mathjax) handled by upgrade_metadata_v8 plugin |

## Plugin Status

| Plugin | Status | Notes |
|---|---|---|
| `rest_html5` | **Disabled** | Present in `plugins/` but NOT in `COMPILERS` in conf.py. Use original `rest` compiler + keep it in POSTS/PAGES if needed. |
| `less` | **Not active** | Plugin present but no `less/targets` file found; bootblog4 theme has no LESS sources. |
| `upgrade_metadata_v8` | **Migration tool** | One-time converter for v7→v8 tags (`draft`, `private`, `mathjax` → `status`, `has_math`). Remove after upgrade. |

## Testing & Verification

```bash
# Check links and files in generated site
nikola check -l

# Full build + confirm success
nikola build && echo "Build OK"

# Serve and auto-reload
nikola serve -b   # opens browser

# Deploy (CI triggers on push to master)
# GitHub Actions: getnikola/nikola-action@v8
# Deploys to gh-pages branch (configured in conf.py)
```

## Nikola Handbook Reference

For deeper configuration or migrating to newer Nikola versions, see:
- <https://getnikola.com/handbook.html>
- `nikola help <command>` for task-specific usage
- `nikola new_post --available-formats` to list supported input formats

Key areas to watch when porting config:
- `COMPILERS` dict — which input formats are active
- `POSTS` / `PAGES` tuples — which extensions are scanned
- `THEME_CONFIG` — theme-specific bootblog4 options
- `DEPLOY_COMMANDS` — custom deploy presets
- `GITHUB_*` settings — GitHub Pages integration