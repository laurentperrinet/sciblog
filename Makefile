default: deploy

build:
	nikola build

deploy: build
	nikola deploy
