all: help

help:  ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

start: ## Start debug server
    uvicorn main:app --reload

start_celery: ## Start celery worker
    celery -A app.celery worker --loglevel=info --pool=solo

makemigrations: # Generate migration files
	alembic revision --autogenerate

migrate:
	alembic upgrade head
