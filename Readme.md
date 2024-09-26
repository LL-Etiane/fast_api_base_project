# Base folder structure for my fast api projects
## How to run 
1 create your virtual environment and activate it
2 install requirements.txt file. 
3 Copy .env.example to .env and set the correct values
4 The project use makefile to automate running commands. You can type `make ` to see the available commands. For example 
    - to start the server user `mak start`  
    - to start celery `make start_celery`
    - to generate migrations, `make migrations`
    - to migrate the migrations, `make migrate`