#!/bin/bash
cd "$(dirname "$0")"

[ -z "$DB_VERSION" ] && DB_VERSION="notset"
[ -z "$POSTGRES_HOST" ] && POSTGRES_HOST=pglocal
[ -z "$POSTGRES_PORT" ] && POSTGRES_PORT=5432
[ -z "$POSTGRES_DB" ] && POSTGRES_DB="metrics"
[ -z "$POSTGRES_SCHEMA" ] && POSTGRES_SCHEMA="kudosbot"
[ -z "$POSTGRES_OPTIONS" ] || POSTGRES_OPTIONS="&$POSTGRES_OPTIONS"

echo "setting up database [${POSTGRES_DB}] if it doesn't exist"
echo "/create-database.sh ${POSTGRES_HOST} ${POSTGRES_DB}"
/create-database.sh ${POSTGRES_HOST} ${POSTGRES_DB}

current_ver=$(migrate -database "postgresql://${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}?x-migrations-table=${POSTGRES_SCHEMA}_schema_migrations${POSTGRES_OPTIONS}" -path /db-versions version)
echo "pre migrate db version is : $current_ver"

if [ $DB_VERSION == "notset" ]
then
  echo "now applying all migration steps..."
  migrate -database "postgresql://${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}?x-migrations-table=${POSTGRES_SCHEMA}_schema_migrations${POSTGRES_OPTIONS}" -path /db-versions up
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
  echo "migrate -database \"postgresql://${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}?x-migrations-table=${POSTGRES_SCHEMA}_schema_migrations${POSTGRES_OPTIONS}\" -path /db-versions goto ${DB_VERSION}"
  migrate -database "postgresql://${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}?x-migrations-table=${POSTGRES_SCHEMA}_schema_migrations${POSTGRES_OPTIONS}" -path /db-versions goto ${DB_VERSION}
  exit_code=$?
  if [ $exit_code -eq 0 ]
  then
    echo "Successfully run migrations steps"
  else
    echo "Failed to run migration steps exit code $exit_code" >&2
    exit 1
  fi
fi

current_ver=$(migrate -database "postgresql://${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}?x-migrations-table=${POSTGRES_SCHEMA}_schema_migrations${POSTGRES_OPTIONS}" -path /db-versions version)
echo "post migrate db version is : $current_ver"
exit 0
