from django.db import models
from django.conf import settings
from product.models import Product


class FulfillmentEvent(models.Model):
    target_date = models.DateField()

    def __str__(self):
        return self.target_date.strftime(settings.DISPLAY_DATE_FORMAT)

class Order(models.Model):
    DEFAULT_USER_ID = 1

    class FulfillmentMethod(models.TextChoices):
        DELIVERY = settings.FULFILLMENT_METHODS_DELIVERY
        COLLECTION = settings.FULFILLMENT_METHODS_COLLECTION

    class CollectionLocation(models.TextChoices):
        DENBIES = settings.COLLECTION_LOCATIONS_DENBIES
        OCKLEY = settings.COLLECTION_LOCATIONS_OCKLEY

    customer_name = models.CharField(max_length=512)
    customer_address = models.CharField(max_length=512)
    customer_postcode = models.CharField(max_length=8)
    customer_email = models.EmailField(max_length=64)
    customer_phone = models.CharField(max_length=64)
    fulfillment_method = models.CharField(choices=FulfillmentMethod.choices, max_length=16)
    collection_location = models.CharField(choices=CollectionLocation.choices, max_length=16, blank='N/A')
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
        blank=False,
        null=False
    )
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f'{self.customer_name}: {self.customer_postcode} by {self.fulfillment_method}'
