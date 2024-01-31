dependencies:
	@echo "Installing prerequisites..."
	pip install poetry
	pip install pre-commit
	@echo "Installing dependencies..."
	poetry install
	poetry run pre-commit install

env: dependencies
	@echo "Activating virtual environment..."
	poetry shell