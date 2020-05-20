import re
from django.db import migrations
from django.conf import settings
from django.utils import timezone
from djmoney.money import Money
from product.fixtures import initial_products
from shared.environments import create_product_fixtures


def reverse_migration(apps, schema_editor):
    pass


def add_default(apps, schema_editor):
    create_product_fixtures()

class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_default, reverse_code=reverse_migration),
    ]
