from django.db import migrations
from shared.environments import create_sample_orders
from product.models import Product
from order.models import Order
from django.core.exceptions import ValidationError


def reverse_migration(apps, schema_editor):
    pass


def add_default(apps, schema_editor):
    product_count = len(Product.objects.all())
    order_count = len(Order.objects.all())
    if product_count > 0 and order_count > 0:
        print(
            "\nNot creating sample orders/events/products\nThere are already products and orders in the database."
        )
    else:
        create_sample_orders()


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0006_auto_20201008_0822"),
    ]

    operations = [
        migrations.RunPython(add_default, reverse_code=reverse_migration),
    ]
