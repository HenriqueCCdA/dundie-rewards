.PHONY: install virtualenv python clean test

install:
	@echo "Installing for dev environment"
	@.venv/bin/python -m pip install -e '.[dev]'


virtualenv:
	@python -m pip -m venv .venv --upgrade-deps

ipython:
	@.venv/bin/ipython

test:
	@.venv/bin/pytest -s

watch:
	# @.venv/bin/ptw -- -s
	@ls **/*.py | entr pytest

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
