from djmoney.models.fields import MoneyField
from django.conf import settings
from django.db import models

class Product(models.Model):

    class Category(models.TextChoices):
        VEGBAG = settings.PRODUCT_CATEGORIES_VEGBAG
        ITEM = settings.PRODUCT_CATEGORIES_ITEM

    name = models.CharField(max_length=256)
    slug = models.CharField(max_length=64)
    pack_size = models.CharField(max_length=256)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency=settings.DEFAULT_CURRENCY)
    published = models.BooleanField(default=True)
    sequence = models.IntegerField()
    category = models.CharField(choices=Category.choices, max_length=16)
    
    def __str__(self):
        return self.name