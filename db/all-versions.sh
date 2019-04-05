#!/bin/bash
cd "$(dirname "$0")"
echo "Running kudosbot schema migration steps"

[ -z "$PG_HOSTNAME" ] && PG_HOSTNAME=pglocal
[ -z "$PG_PORT" ] && PG_PORT=5432
[ -z "$PG_DATABASE" ] && PG_DATABASE="metrics"
[ -z "$PG_SCHEMA" ] && PG_SCHEMA="kudosbot"
[ -z "$PG_OPTIONS" ] || PG_OPTIONS="&$PG_OPTIONS"

echo "setting up database if it doesn't exist"
./create-database.sh $PG_HOSTNAME $PG_DATABASE

ver=$(migrate -database "postgresql://${PG_HOSTNAME}:${PG_PORT}/${PG_DATABASE}?x-migrations-table=${PG_SCHEMA}_schema_migrations${PG_OPTIONS}" -path /db-versions version)
echo "current version : $ver"

echo "now applying all migration steps..."
migrate -database "postgresql://${PG_HOSTNAME}:${PG_PORT}/${PG_DATABASE}?x-migrations-table=${PG_SCHEMA}_schema_migrations${PG_OPTIONS}" -path /db-versions up
