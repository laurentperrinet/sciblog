default: deploy

build:
	nikola build

deploy: build
	nikola deploy

github_deploy: build
	nikola github_deploy
