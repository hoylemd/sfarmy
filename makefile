PROJECT_NAME=hs_sim
CORE_APP_NAME=hs_sim
CORE_APP_PATH=app/$(CORE_APP_NAME)
MANAGE=python app/manage.py

all: go

go: app/manage.py
	$(MANAGE) runserver

migrate: app/manage.py
	$(MANAGE) migrate

migrations: app/manage.py
	$(MANAGE) makemigrations

first_time_dev_setup: scripts/first_time.sh
	scripts/first_time.sh
