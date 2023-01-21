.PHONY: install virtualenv ipython lint fmt test watch docs build publish-test clean

install:
	@echo "Installing for dev environment"
	@.venv/bin/python -m pip install -e '.[dev]'

virtualenv:
	@python -m pip -m venv .venv --upgrade-deps

ipython:
	@.venv/bin/ipython

lint:
	@.venv/bin/pflake8

fmt:
	@.venv/bin/isort dundie integration tests
	@.venv/bin/black dundie integration tests

test:
	@.venv/bin/pytest -s --forked

watch:
	# @.venv/bin/ptw -- -s
	@ls **/*.py | entr pytest --forked

docs:
	@mkdocs build --clean


build:
	@python setup.py sdist bdist_wheel

publish-test:
	@twine upload -- repository testpypi dist/*

clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '__pycache__' -exec rm -rf {} \;
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf htmlcov
