environment = development
test_pattern = *
code_folder = api

install:
	@make -s check
	@ln -sfr dockerfiles/docker-compose.$(environment).yml docker-compose.yml
	@make decrypt environment=$(environment)
	@ln -sfr configs/environments/$(environment).env .env
	docker-compose up -d
	@ln -sfr configs/environments/$(environment).env $(code_folder)/.env
	cd $(code_folder) && make install

pip_install:
	cd $(code_folder) && make pip_install

migrate:
	cd $(code_folder) && make migrate

build:
	@make -s check
	@make decrypt environment=$(environment)
	@ln -sfr configs/environments/$(environment).env .env
	@ln -sfr dockerfiles/docker-compose.$(environment).yml docker-compose.$(environment).yml
	docker-compose -f docker-compose.$(environment).yml build --pull

up:
	@make -s check
	@make decrypt environment=$(environment)
	@ln -sfr config/environments/$(environment).env .env
	docker-compose -f docker-compose.$(environment).yml up -d --build

backend_shell:
	docker-compose exec $(code_folder) bash

test:
	docker-compose exec $(code_folder) python manage.py test --pattern="$(test_pattern)"

encrypt:
	@openssl enc -aes-256-cbc -salt -e -k "${CRYPTO_SECRET_KEY}" -in configs/environments/$(environment).env -out configs/environments/$(environment).crp

decrypt:
	@openssl enc -aes-256-cbc -salt -d -k "${CRYPTO_SECRET_KEY}" -in configs/environments/$(environment).crp -out configs/environments/$(environment).env

check:
	@if [ ! "$(environment)" = "development" -a ! "$(environment)" = "stage" -a ! "$(environment)" = "production" ]; then\
		echo "Environment should be development or production";\
		exit 1;\
	fi

	@if [ ! $(shell command -v docker-compose 2> /dev/null) ]; then\
		echo "You should install docker-compose";\
		exit 1;\
	fi

	@if [ "$(environment)" = "production" -a ! config/environments/production.env ]; then\
		echo "File production.env doesn't exist";\
		exit 1;\
	fi
