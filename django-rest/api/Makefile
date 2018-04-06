venv=python3
environment = development

install:
	@make -s check
	[ -d $(venv) ] || virtualenv -p python3.6 $(venv)
	@make pip_install venv=$(venv) environment=$(environment)
	@make migrate

pip_install:
	$(venv)/bin/pip install -r requirements.txt

migrate:
	$(venv)/bin/python manage.py makemigrations
	$(venv)/bin/python manage.py migrate

check:
	@if [ ! "$(environment)" = "development" -a ! "$(environment)" = "production" ]; then\
		echo "Environment should be development or production";\
		exit 1;\
	fi

	@if [ -a .env ]; then\
		echo "File .env doesn't exist";\
		exit 1;\
	fi
