from django.db import models
from django.conf import settings
from product.models import Product
from django.utils import timezone


class FulfillmentEvent(models.Model):
    target_date = models.DateField()

    def __str__(self):
        return self.target_date.strftime(settings.DISPLAY_DATE_FORMAT)

    @property
    def orders_count(self):
        """Return count annotation if any else re-count transactions."""
        count = getattr(self, 'orders__count', None)
        if count is None:
            count = self.order_set.count()
        return count

class Order(models.Model):
    DEFAULT_USER_ID = 1

    class FulfillmentMethod(models.TextChoices):
        DELIVERY = settings.FULFILLMENT_METHODS_DELIVERY
        COLLECTION = settings.FULFILLMENT_METHODS_COLLECTION

    class CollectionLocation(models.TextChoices):
        DENBIES = settings.COLLECTION_LOCATIONS_DENBIES
        OCKLEY = settings.COLLECTION_LOCATIONS_OCKLEY

    customer_name = models.CharField(max_length=512, verbose_name='Name')
    customer_address = models.CharField(max_length=512, verbose_name='Address')
    customer_postcode = models.CharField(max_length=8, verbose_name='Postcode')
    customer_email = models.EmailField(max_length=64, verbose_name='Email')
    customer_phone = models.CharField(max_length=64, verbose_name='Phone')
    fulfillment_method = models.CharField(choices=FulfillmentMethod.choices, max_length=16, verbose_name='DELIVERY / COLLECTION')
    collection_location = models.CharField(choices=CollectionLocation.choices, max_length=16, blank='N/A', verbose_name='If collection, which shop?')
    notes = models.TextField(blank=True, verbose_name='NOTES')
    archived = models.BooleanField(default=False)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        default=DEFAULT_USER_ID,
        blank=False,
        null=True
    )

    fulfillment_event = models.ForeignKey(
        FulfillmentEvent,
        on_delete=models.CASCADE,
        # default=MOST_RECENT_EVENT
        blank=False,
        null=False
    )
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f'{self.customer_name}: {self.customer_postcode} by {self.fulfillment_method}'

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.created_at = timezone.now()
    #         self.modified_at = timezone.now()

    def product_count(self, id):
        return self.products.filter(id=id).count()
