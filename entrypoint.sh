#!/bin/ash


echo "applying migrations"
python manage.py migrate

exec "$@"

