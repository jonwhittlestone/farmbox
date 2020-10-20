from django.db import migrations
from django.core.management import call_command
from django.core.exceptions import ValidationError

import logging

logger = logging.getLogger(__name__)


def reverse_migration(apps, schema_editor):
    pass


def add_default(apps, schema_editor):
    call_command(
        "create_customers_from_orders",
    )


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0007_create_sample_orders"),
    ]

    operations = [
        migrations.RunPython(add_default, reverse_code=reverse_migration),
    ]
