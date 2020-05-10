clean:
	@echo "Cleaning up ..."
	@find . -type f -name "*.py[co]" -delete
	@find . -type d -name "__pycache__" -delete
	@find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} +
	@find . -type d -name ".pytest_cache" -exec rm -rf {} +

format_black:
	@echo "Black formatting ..."
	@poetry run black .

format_prettier:
	@echo "Prettier formatting ..."
	@npx prettier --write $$(find \( -name "*.yml" -o -name "*.yaml" -o -name "*.json" \) -not \( -path "./.venv/*" -o -path "./.tox/*" \))

format: format_black format_prettier clean

lint_black:
	@echo "Black linting ..."
	@poetry run black --check .

lint_pylint:
	@echo "Pylint linting ..."
	@poetry run pylint $$(find \( -name "*.py" \) -not \( -path "./.venv/*" -o -path "./.tox/*" -o -path "*/**/.venv/*" -o -path "./notebooks/*" \))

lint_prettier:
	@echo "Prettier linting ..."
	@npx prettier --check $$(find \( -name "*.yml" -o -name "*.yaml" -o -name "*.json" \) -not \( -path "./.venv/*" -o -path "./.tox/*" \))

lint: lint_black lint_pylint clean
