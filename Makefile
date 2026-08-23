.PHONY: install dev lint mypy bandit test cov mutate build release

PYTHON ?= python3

install:
	$(PYTHON) -m pip install .

dev:
	$(PYTHON) -m pip install -e ".[dev]"

lint:
	ruff check lazyaddon tests

mypy:
	mypy lazyaddon

bandit:
	bandit -r lazyaddon

test:
	pytest -q

cov:
	pytest --cov=lazyaddon --cov-report=term-missing -q

mutate:
	mutmut run --paths-to-mutate "lazyaddon/models.py lazyaddon/placeholders.py lazyaddon/security.py"

build:
	rm -rf dist build
	python -m build

release:
	python -m twine upload dist/*
