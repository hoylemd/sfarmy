PROJECT_NAME=sfarmy
CORE_APP_NAME=sfarmy
CORE_APP_PATH=$(PROJECT_NAME)/$(CORE_APP_NAME)
MANAGE=python $(PROJECT_NAME)/manage.py

all: go

go: $(PROJECT_NAME)/manage.py
	$(MANAGE) runserver

migrate: $(PROJECT_NAME)/manage.py
	$(MANAGE) migrate
