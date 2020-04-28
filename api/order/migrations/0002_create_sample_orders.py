import random
from django.db import migrations
from django.conf import settings
from django.utils import timezone
from product.models import Product
from order.models import Order, FulfillmentEvent
from order.fixtures import sample_fulfillment_events, sample_orders

NUMBER_PRODUCTS_TO_ADD_TO_A_SAMPLE_ORDER = 5

def reverse_migration(apps, schema_editor):
    pass


def add_default(apps, schema_editor):

    # We can't import the model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    # Event_Model = apps.get_model('order', 'FulfillmentEvent')
    for evt in sample_fulfillment_events:
        new_evt = FulfillmentEvent(**evt)
        new_evt.save()

    Order_Model = apps.get_model('order', 'Order')
    for order in sample_orders:
        order['user_id'] = 1
        order['fulfillment_event_id'] = new_evt.id
        ord = Order_Model(**order)
        ord.save()

    
    # add sample products
    for ord in Order.objects.all():
        valid_products_ids = Product.objects.all().values_list('id', flat=True)
        ids = list(valid_products_ids)
        random_products_ids = random.sample(ids, min(len(ids), NUMBER_PRODUCTS_TO_ADD_TO_A_SAMPLE_ORDER))

        qs = Product.objects.filter(id__in=random_products_ids)
        for p in qs:
            from order.models import ProductQuantity
            ProductQuantity.objects.create(order=ord, product=p, quantity=random.randint(1,3))
    #         ord.products.add(p)


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_default, reverse_code=reverse_migration),
    ]
