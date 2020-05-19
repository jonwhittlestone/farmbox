import re
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
        try:
            p = Product_Model(**product)
            p.code = re.findall('[A-Z]{2}[0-9]*$',p.name)[0]
            p.save()
        except Exception as e:
            print(p.code)

class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_default, reverse_code=reverse_migration),
    ]
