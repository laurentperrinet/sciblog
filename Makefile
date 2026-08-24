all: default
default: build

build:
	nikola build

serve:
	nikola serve

clean:
	nikola clean

update:
	pip install -U -r requirements.txt