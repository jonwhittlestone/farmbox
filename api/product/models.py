from djmoney.models.fields import MoneyField
from django.conf import settings
from django.db import models


class Product(models.Model):

    class Category(models.TextChoices):
        VEGBAG = settings.PRODUCT_CATEGORIES_VEGBAG
        ITEM = settings.PRODUCT_CATEGORIES_ITEM

    name = models.CharField(max_length=256)
    code = models.CharField(max_length=64)
    pack_size = models.CharField(max_length=256)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency=settings.DEFAULT_CURRENCY)
    published = models.BooleanField(default=True)
    sequence = models.PositiveSmallIntegerField(default=0, blank=False, null=False)
    category = models.CharField(choices=Category.choices, max_length=16)

    def __str__(self):
        return f'{self.name}'

    @classmethod
    def published_names(cls):
        qs = cls.objects.filter(published=True)
        product_names = list(qs.values_list('name', flat=True))
        product_ids = list(qs.values_list('id', flat=True))
        ids_names = list(qs.values('id','name'))
        return [p.get('name') for p in ids_names], [p.get('id') for p in ids_names]

    def quantity(self):

        qs = self.product_quantities.filter(product_id=product_id).first()
        if qs:
            return qs.quantity
        return 0

    class Meta:
        ordering = ('sequence',)

class ProductSelection(models.Model):

    name = models.CharField(max_length=256)
    active = models.BooleanField(default=False)
    products = models.ForeignKey(Product, on_delete=models.SET_NULL)
    created_at = models.DateTimeField()
