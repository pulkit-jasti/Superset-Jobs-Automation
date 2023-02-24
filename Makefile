run: ## Run main app
	python app.py

install: ## Install dependencies
	pip install -r requirements.txt

freeze: ## Updates requirements file with installed dependencies
	pip freeze > requirements.txt