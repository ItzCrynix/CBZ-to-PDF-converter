.PHONY: run venv all

venv: init_venv.sh
	bash ./init_venv.sh

run:
	./venv/bin/python main.py || ./venv/Scripts/python main.py

all: venv run