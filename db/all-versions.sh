#!/bin/bash
cd "$(dirname "$0")"
echo "Running kudosbot schema migration steps"

[ -z "$POSTGRES_HOST" ] && POSTGRES_HOST=localhost
[ -z "$POSTGRES_PORT" ] && POSTGRES_PORT=5432
[ -z "$POSTGRES_DB" ] && POSTGRES_DB="metrics"
[ -z "$POSTGRES_SCHEMA" ] && POSTGRES_SCHEMA="kudosbot"
[ -z "$POSTGRES_OPTIONS" ] || POSTGRES_OPTIONS="&$POSTGRES_OPTIONS"

echo "setting up database if it doesn't exist"
./create-database.sh $POSTGRES_HOST $POSTGRES_DB

ver=$(migrate -database "postgresql://${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}?x-migrations-table=${POSTGRES_SCHEMA}_schema_migrations${POSTGRES_OPTIONS}" -path /db-versions version)
echo "current version : $ver"

echo "now applying all migration steps..."
migrate -database "postgresql://${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}?x-migrations-table=${POSTGRES_SCHEMA}_schema_migrations${POSTGRES_OPTIONS}" -path /db-versions up
