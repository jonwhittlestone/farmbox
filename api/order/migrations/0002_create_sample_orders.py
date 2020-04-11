import random
from django.db import migrations
from django.conf import settings
from django.utils import timezone
from product.models import Product
from order.models import Order

NUMBER_PRODUCTS_TO_ADD_TO_A_SAMPLE_ORDER = 5

sample_orders = [
    {
        'customer_name': '[NotARealOrder] Christopher Koliba',
        'customer_address': '11 Lonsdale Place, Dorking',
        'customer_postcode': 'RH4 2WJ',
        'customer_email': 'dev+farmbox@howapped.com',
        'customer_phone': '0789 449 5422',
        'fulfillment_method': 'Delivery',
        'collection_location': 'Denbies',
        'customer_specified_fulfilled_at': '2020-05-01 06:08:45.204004+00:00',
        'created_at': timezone.now(),
        'modified_at': timezone.now(),
    },

    {
        'customer_name': '[NotARealOrder] Mike Jameson',
        'customer_address': '12 Curtis Road, Dorking',
        'customer_postcode': 'RH4 1XD',
        'customer_email': 'dev+farmbox@howapped.com',
        'customer_phone': '0789 449 5422',
        'fulfillment_method': 'Collection',
        'collection_location': 'Denbies',
        'customer_specified_fulfilled_at': '2020-05-01 06:08:45.204004+00:00',
        'created_at': timezone.now(),
        'modified_at': timezone.now(),
    },

    {
        'customer_name': '[NotARealOrder] Valerie Bennet',
        'customer_address': 'Cotton Row, Holmbury St. Mary',
        'customer_postcode': 'RH5 6NB',
        'customer_email': 'dev+farmbox@howapped.com',
        'customer_phone': '0789 449 5422',
        'fulfillment_method': 'Delivery',
        'collection_location': '',
        'customer_specified_fulfilled_at': '2020-05-01 06:08:45.204004+00:00',
        'created_at': timezone.now(),
        'modified_at': timezone.now(),
    },

    {
        'customer_name': '[NotARealOrder] Chloe Fawcett',
        'customer_address': 'Dial Post Barn, Horsham, West Sussex',
        'customer_postcode': 'RH12 4QX',
        'customer_email': 'dev+farmbox@howapped.com',
        'customer_phone': '0789 449 5422',
        'fulfillment_method': 'Collection',
        'collection_location': 'Ockley',
        'customer_specified_fulfilled_at': '2020-05-01 06:08:45.204004+00:00',
        'created_at': timezone.now(),
        'modified_at': timezone.now(),
    }
]

def reverse_migration(apps, schema_editor):
    pass


def add_default(apps, schema_editor):

    # We can't import the model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Order_Model = apps.get_model('order', 'Order')
    for order in sample_orders:
        order['user_id'] = 1
        ord = Order_Model(**order)
        ord.save()

    
    # add sample products
    for ord in Order.objects.all():
        valid_products_ids = Product.objects.all().values_list('id', flat=True)
        ids = list(valid_products_ids)
        random_products_ids = random.sample(ids, min(len(ids), NUMBER_PRODUCTS_TO_ADD_TO_A_SAMPLE_ORDER))
        qs = Product.objects.filter(id__in=random_products_ids)
        for p in qs:
            ord.products.add(p)


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_default, reverse_code=reverse_migration),
    ]
