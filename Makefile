all: default
default: github_deploy

build:
	nikola build

deploy: build
	echo "Deploying to docs folder (OBSOLETE)..."
	nikola deploy

github_deploy: build
	echo "Deploying to github ..."
	nikola github_deploy

update:
	pip install -U -r requirements.txt
