PROJECT_NAME=""
CORE_APP_NAME=""
CORE_APP_PATH="$(PROJECT_NAME)/$(CORE_APP_NAME)"

all: go

go: $(PROJECT_NAME)/manage.py
	python $(PROJECT_NAME)/manage.py runserver
