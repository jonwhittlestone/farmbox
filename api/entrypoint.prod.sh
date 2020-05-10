#!/usr/bin/env sh
pwd
ls | wc -l
python manage.py migrate
python manage.py collectstatic --no-input --clear
python manage.py runserver
exec "$@"
