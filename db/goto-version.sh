#!/bin/bash
cd "$(dirname "$0")"

[ -z "$DB_VERSION" ] && DB_VERSION="notset"
[ -z "$PG_HOSTNAME" ] && PG_HOSTNAME=pglocal
[ -z "$PG_PORT" ] && PG_PORT=5432
[ -z "$PG_DATABASE" ] && PG_DATABASE="metrics"
[ -z "$PG_SCHEMA" ] && PG_SCHEMA="kudosbot"
[ -z "$PG_OPTIONS" ] || PG_OPTIONS="&$PG_OPTIONS"

echo "setting up database [${PG_DATABASE}] if it doesn't exist"
echo "/create-database.sh ${PG_HOSTNAME} ${PG_DATABASE}"
/create-database.sh ${PG_HOSTNAME} ${PG_DATABASE}

current_ver=$(migrate -database "postgresql://${PG_HOSTNAME}:${PG_PORT}/${PG_DATABASE}?x-migrations-table=${PG_SCHEMA}_schema_migrations${PG_OPTIONS}" -path /db-versions version)
echo "pre migrate db version is : $current_ver"

if [ $DB_VERSION == "notset" ]
then
  echo "now applying all migration steps..."
  migrate -database "postgresql://${PG_HOSTNAME}:${PG_PORT}/${PG_DATABASE}?x-migrations-table=${PG_SCHEMA}_schema_migrations${PG_OPTIONS}" -path /db-versions up
  exit_code=$?
  if [ $exit_code -eq 0 ]
  then
    echo "Successfully run migrations steps"
  else
    echo "Failed to run migration steps exit code $exit_code" >&2
    exit 1
  fi

else
  echo "now applying all migration steps to $DB_VERSION"
  echo "migrate -database \"postgresql://${PG_HOSTNAME}:${PG_PORT}/${PG_DATABASE}?x-migrations-table=${PG_SCHEMA}_schema_migrations${PG_OPTIONS}\" -path /db-versions goto ${DB_VERSION}"
  migrate -database "postgresql://${PG_HOSTNAME}:${PG_PORT}/${PG_DATABASE}?x-migrations-table=${PG_SCHEMA}_schema_migrations${PG_OPTIONS}" -path /db-versions goto ${DB_VERSION}
  exit_code=$?
  if [ $exit_code -eq 0 ]
  then
    echo "Successfully run migrations steps"
  else
    echo "Failed to run migration steps exit code $exit_code" >&2
    exit 1
  fi
fi

current_ver=$(migrate -database "postgresql://${PG_HOSTNAME}:${PG_PORT}/${PG_DATABASE}?x-migrations-table=${PG_SCHEMA}_schema_migrations${PG_OPTIONS}" -path /db-versions version)
echo "post migrate db version is : $current_ver"
exit 0
