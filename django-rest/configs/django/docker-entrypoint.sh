#!/usr/bin/env bash

set -e

echo "Starting up Api server of ${PROJECT_NAME} project in $ENVIRONMENT environment"

echo "Waiting for Postgres"
wait-for-it.sh \
	--host=${POSTGRES_HOST} \
	--port=${POSTGRES_PORT} \
	--timeout=15 \
	--strict \
	-- echo "Postgres is up"

echo "Waiting for Redis"
wait-for-it.sh \
	--host=${REDIS_HOST} \
	--port=${REDIS_PORT} \
	--timeout=15 \
	--strict \
	-- echo "Redis is up"

case "$ENVIRONMENT" in
	"development" | "stage" | "production")
	    ;;
	*)
		echo "Variable ENVIRONMENT has unsupported value: $ENVIRONMENT"
		exit 1
		;;
esac

export DJANGO_SETTINGS_MODULE=project.settings
echo "Variable DJANGO_SETTINGS_MODULE is set to $DJANGO_SETTINGS_MODULE value"

# Migrations should exist before building image in production mode
echo "Creating migrations"
if [ "$ENVIRONMENT" = "development" ]; then
    python manage.py makemigrations
fi

echo "Applying migrations"
python manage.py migrate && python manage.py migrate --run-syncdb

echo "Collecting static files"
python manage.py collectstatic --no-input --clear

echo "Starting $@"
exec $@
