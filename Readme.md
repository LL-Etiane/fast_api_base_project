# Base folder structure for my FastAPI projects

## How to run

1. Create your virtual environment and activate it.
2. Install the requirements from the `requirements.txt` file.
3. Copy `.env.example` to `.env` and set the correct values.
4. The project uses a Makefile to automate running commands. You can type `make` to see the available commands. For example:
    - To start the server, use `make start`.
    - To start Celery, use `make start_celery`.
    - To generate migrations, use `make migrations`.
    - To migrate the migrations, use `make migrate`.