#!/usr/bin/env sh

set -e

echo "Starting Nginx server"

echo "Waiting for Api"
/opt/bin/wait-for-it.sh \
	--host=${SERVER_HOST} \
	--port=${SERVER_PORT} \
	--timeout=15 \
	--strict \
	-- echo "Backend is up"

echo "Create cache dirs"
mkdir -p /var/lib/nginx/cache /var/lib/nginx/proxy

exec $@
