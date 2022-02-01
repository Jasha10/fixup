test:
	black src tests
	isort src tests
	dmypy run src tests
	pyflakes .
	pylint
	pytest
	pyright
