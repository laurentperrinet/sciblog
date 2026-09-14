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