from django.db import migrations
from django.conf import settings
from django.utils import timezone


def reverse_migration(apps, schema_editor):
    pass


def add_default(apps, schema_editor):
    from django.contrib.auth import get_user_model; 
    User = get_user_model(); 
    User.objects.create_superuser(settings.DEFAULT_SUPERUSER.get(
        'username', ''), settings.DEFAULT_SUPERUSER.get(
        'email', ''), settings.DEFAULT_SUPERUSER.get(
        'password', ''))

class Migration(migrations.Migration):
    dependencies = []

    operations = [
        migrations.RunPython(add_default, reverse_code=reverse_migration),
    ]
