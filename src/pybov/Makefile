SHELL := /bin/bash

test/code:
	@poetry run mypy --strict src/

test/pytest:
	@poetry run python -m pytest test/

test: test/code test/pytest

.PHONY: test/code test/unit test
