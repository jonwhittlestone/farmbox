from django.db import migrations
from django.conf import settings
from django.utils import timezone
from djmoney.money import Money
from product.fixtures import initial_products


def reverse_migration(apps, schema_editor):
    pass


def add_default(apps, schema_editor):

    # We can't import the model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Product_Model = apps.get_model('product', 'Product')
    for product in initial_products:
        p = Product_Model(**product)
        p.save()

class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_default, reverse_code=reverse_migration),
    ]
