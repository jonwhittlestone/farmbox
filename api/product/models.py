import re
import logging
from django.db.models import F
from djmoney.models.fields import MoneyField
from django.conf import settings
from django.db import models

logger = logging.getLogger(__name__)


class ProductQuerySet(models.QuerySet):
    def published(self):
        return self.filter(published=True).order_by("sequence")


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)


class Product(models.Model):
    class Category(models.TextChoices):
        VEGBAG = settings.PRODUCT_CATEGORIES_VEGBAG
        ITEM = settings.PRODUCT_CATEGORIES_ITEM

    name = models.CharField(max_length=256)
    code = models.CharField(max_length=64)
    pack_size = models.CharField(max_length=256, default=Category.ITEM)
    price = MoneyField(
        max_digits=14, decimal_places=2, default_currency=settings.DEFAULT_CURRENCY
    )
    published = models.BooleanField(default=False)
    sequence = models.PositiveSmallIntegerField(default=0, blank=False, null=False)
    category = models.CharField(
        choices=Category.choices, max_length=16, default=Category.ITEM
    )

    objects = ProductManager()

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def published_names(cls):
        qs = cls.objects.filter(published=True)
        ids_names = list(qs.values("id", "name"))
        return [p.get("name") for p in ids_names], [p.get("id") for p in ids_names]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        try:
            self.code = re.findall("[A-Z]{2}[0-9]*$", self.name)[0]
            super().save(*args, **kwargs)
        except Exception as e:
            print(self.code)
            print(e)

    @classmethod
    def write_new_selection(cls, selection):
        """
        Given a new selection, ensures new products are written,
        and correct sequence is updated
        """
        products = []
        # validate entry
        # unpublish all, and temporary resequence
        Product.objects.update(published=False, sequence=F("sequence") + 1000)
        # for each product
        for i, s in enumerate(selection):
            if not Product.objects.filter(code=s.get("code")).exists():
                p = Product(**s)
                p.sequence = i + 1
                p.published = True
            else:
                try:
                    p = Product.objects.get(code=s.get("code"))
                    p.name = s.get("name")
                    p.price = s.get("price")
                    p.sequence = i + 1
                    p.published = True
                except Exception:
                    logger.info(p)
                    continue
            products.append(p)

        for p in products:
            p.save()

        persisted_selection = list(Product.objects.all().published().values())
        return persisted_selection

    class Meta:
        ordering = ("sequence",)
