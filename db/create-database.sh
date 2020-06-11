#!/bin/bash
HOSTNAME=$1
DATABASE=$2

echo "Creating database $2 on using connection $1 if it does not exist.."
psql -tc "SELECT 1 FROM POSTGRES_DB WHERE datname = '$2'" --host $1 --dbname postgres | grep -q 1 || psql -c "CREATE DATABASE $2" --host $1 --dbname postgres

