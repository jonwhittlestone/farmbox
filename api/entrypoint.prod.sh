#!/usr/bin/env sh
pwd
ls | wc -l
# python manage.py collectstatic --no-input --clear
exec "$@"
