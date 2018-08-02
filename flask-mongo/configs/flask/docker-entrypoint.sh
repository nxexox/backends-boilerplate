#!/usr/bin/env bash

set -e

echo "Starting up Backend server of ${PROJECT_NAME} project in $ENVIRONMENT environment"

echo "Waiting for Mongo"
wait-for-it.sh \
	--host=${MONGO_HOST} \
	--port=${MONGO_PORT} \
	--timeout=15 \
	--strict \
	-- echo "Postgres is up"

case "$ENVIRONMENT" in
	"development" | "stage" | "production")
	    ;;
	*)
		echo "Variable ENVIRONMENT has unsupported value: $ENVIRONMENT"
		exit 1
		;;
esac

echo "Starting $@"
exec $@
