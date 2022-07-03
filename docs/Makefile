SHELL := /bin/bash

docs/html:
	@sphinx-build -M html source/ build/

docs/clean:
	@rm -rf build/

docs: docs/clean docs/html

.PHONY: docs/clean docs/html docs
