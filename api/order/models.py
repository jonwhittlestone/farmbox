import os
from django.db import models
from django.conf import settings
from django.utils import timezone


class OrderForm(models.Model):
    filename = models.CharField(max_length=512)

    fulfillment_event = models.ForeignKey(
        'FulfillmentEvent',
        on_delete=models.CASCADE,
        # default=MOST_RECENT_EVENT
        blank=True,
        null=True
    )

    order = models.ForeignKey(
        'order',
        on_delete=models.CASCADE,
        null=True,
        default=None,
        verbose_name='Order Succesfully Created?'
    )

    created_at = models.DateTimeField()


    def __str__(self):
        return f'{os.path.basename(self.filename)} uploaded at {self.created_at}'

class OrderFormFailure(models.Model):
    reason = models.TextField()

    form = models.ForeignKey(
        OrderForm,
        on_delete=models.CASCADE,
        null=False,
        verbose_name='Order Form'
    )

    class Meta:
        ordering = ['-id']


class FulfillmentEvent(models.Model):
    target_date = models.DateField()

    def __str__(self):
        return self.target_date.strftime(settings.DISPLAY_DATE_FORMAT)

    @property
    def remote_folder_name(self):
        return self.target_date.strftime(settings.DISPLAY_DATE_FORMAT).replace(' ','-').replace('/','-')

    @classmethod
    def newest_event(cls):
        return cls.objects.order_by('target_date').last()

    @property
    def orders_count(self):
        """Return count annotation if any else re-count transactions."""
        count = getattr(self, 'orders__count', None)
        if count is None:
            count = self.order_set.count()
        return count

    @property
    def orders_count_delivery(self):
        return self.order_set.filter(fulfillment_method=settings.FULFILLMENT_METHODS_DELIVERY).count()

    @property
    def orders_count_collection_denbies(self):
        return self.order_set.filter(fulfillment_method=settings.FULFILLMENT_METHODS_COLLECTION,collection_location=settings.COLLECTION_LOCATIONS_DENBIES).count()

    @property
    def orders_count_collection_ockley(self):
        return self.order_set.filter(fulfillment_method=settings.FULFILLMENT_METHODS_COLLECTION, collection_location=settings.COLLECTION_LOCATIONS_OCKLEY).count()


class Order(models.Model):
    DEFAULT_USER_ID = 1

    class FulfillmentMethod(models.TextChoices):
        DELIVERY = settings.FULFILLMENT_METHODS_DELIVERY
        COLLECTION = settings.FULFILLMENT_METHODS_COLLECTION

    class CollectionLocation(models.TextChoices):
        DENBIES = settings.COLLECTION_LOCATIONS_DENBIES
        OCKLEY = settings.COLLECTION_LOCATIONS_OCKLEY


    f_number = models.CharField(max_length=64, null=True, verbose_name='F-Number', help_text='An event-unique number assigned at order creation to aid in Fulfillment sequencing')
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

    products = models.ManyToManyField(
        'product.Product', through='ProductQuantity', related_name='products')

    def __str__(self):
        return f'{self.customer_name}: {self.customer_postcode} by {self.fulfillment_method}'

    @property
    def new_f_number(self):
        return f'{self.fulfillment_event_id}-XX{self.id}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.f_number = self.new_f_number
        super().save(*args, **kwargs)


    def product_count(self, product_id):
        qs = self.product_quantities.filter(product_id=product_id).first()
        if qs:
            return qs.quantity
        return 0


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['fulfillment_event_id', 'f_number'], name='unique_f_number_per_event')
        ]
        ordering = ['f_number']


class ProductQuantity(models.Model):

    order = models.ForeignKey('order.Order', related_name='product_quantities', on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', related_name='product_quantities', on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)
