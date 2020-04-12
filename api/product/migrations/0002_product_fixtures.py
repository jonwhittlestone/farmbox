from django.db import migrations
from django.conf import settings
from django.utils import timezone
from djmoney.money import Money


initial_products = [
    {
        'name': 'Village Greens Veg Bag : Large',
        'slug': 'village-greens-veg-bag-large',
        'pack_size': '9-10 lines',
        'price': Money(15, settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':1,
        'category': settings.PRODUCT_CATEGORIES_VEGBAG,
    },

    {
        'name': 'Village Greens Veg Bag : Medium',
        'slug': 'village-greens-veg-bag-medium',
        'pack_size': '8-9 lines',
        'price': Money(13, settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':2,
        'category': settings.PRODUCT_CATEGORIES_VEGBAG
    },
    {
        'name': 'Village Greens Veg Bag : Small',
        'slug': 'village-greens-veg-bag-small',
        'pack_size': '7-8 lines',
        'price': Money(11, settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':3,
        'category': settings.PRODUCT_CATEGORIES_VEGBAG
    },

    {
        'name': 'Fine green beans',
        'slug': 'fine-green-beans',
        'pack_size': '250g',
        'price': Money(2.5, settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':4,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'name': 'Brocoli',
        'slug': 'brocoli',
        'pack_size': 'Head appr 250g',
        'price': Money(2.5, settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':4,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'name': 'Butternut Squash',
        'slug': 'butternut-squash',
        'pack_size': '1',
        'price': Money(1, settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':5,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'name': 'Cabbage Hispi',
        'slug': 'cabbage-hispi',
        'pack_size': '1',
        'price': Money(1.3, settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':6,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

    {
        'name': 'Cabbage Savoy',
        'slug': 'cabbage-savoy',
        'pack_size': '1',
        'price': Money(1.95, settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':7,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'name': 'Cabbage Red',
        'slug': 'cabbage-red',
        'pack_size': '1',
        'price': Money(1.3, settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':8,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'name': 'Carrots : loose washed',
        'slug': 'carrots-loose',
        'pack_size': '500g',
        'price': Money(0.8, settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':9,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },
    {
        'name': 'Cauliflower',
        'slug': 'cauliflower',
        'pack_size': '1',
        'price': Money(3.2,settings.DEFAULT_CURRENCY),
        'published': True,
        'sequence':10,
        'category': settings.PRODUCT_CATEGORIES_ITEM
    },

]

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
