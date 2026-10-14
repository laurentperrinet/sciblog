all: default

default: push 

push:
	# no need to build, github does the job for us
	# so let's just commit and push the changes
	llm-commit.sh

build:
	nikola build

serve:
	nikola serve

clean:
	nikola clean

update:
	pip install -U -r requirements.txt

# Rebuild the client-side search index (Pagefind).
#
# `nikola build` already refreshes docs/pagefind/ through the pagefind_index
# plugin, so this target exists for when the index alone is what you want to
# check. The binary is taken from node_modules (after `npm install`) when
# present, otherwise the plugin downloads the pinned release; see the
# PAGEFIND_* block in conf.py.
search: build
	@ls -d docs/pagefind >/dev/null 2>&1 \
		&& du -sh docs/pagefind \
		&& echo "search index OK -> docs/pages/search.html" \
		|| echo "WARNING: docs/pagefind/ is missing, see the build log above"
