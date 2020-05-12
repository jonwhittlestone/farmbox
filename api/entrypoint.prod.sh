#!/usr/bin/env sh
pwd
ls | wc -l
python manage.py collectstatic --no-input --clear
# echo "from django.contrib.auth.models import User; u = User.objects.get(username='admin'); u.set_password('${DEFAULT_SUPERUSER_PASSWORD}'); u.save()" | python manage.py shell
python manage.py restore_db
exec "$@"
