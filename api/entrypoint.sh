#!/usr/bin/env sh
python manage.py collectstatic --no-input --clear
exec "$@"
