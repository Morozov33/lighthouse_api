host ?= 127.0.0.1
port ?= 9999
start: #start uvicorn server for app
	poetry run uvicorn lighthouse.main:app --reload --host $(host) --port $(port)

lint: #linter for code
	poetry run flake8 lighthouse tests

test: #start pytest
	poetry run pytest

coverage: #start code coverage and write report is xml-file for CodeClimate
	poetry run pytest --cov-report xml --cov=menu_app tests/
