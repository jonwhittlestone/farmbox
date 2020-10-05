from django.db import models


def get_or_create_customer(order_details):
    return {"id": 1, "name": "Jon"}


# Create your models here.
class Customer(models.Model):

    first_name = models.CharField(
        max_length=512, verbose_name="First Name", blank=False
    )
    last_name = models.CharField(max_length=512, verbose_name="Last Name", blank=False)
    address = models.CharField(max_length=512, verbose_name="Address", blank=False)
    postcode = models.CharField(max_length=8, verbose_name="Postcode", blank=False)
    email = models.EmailField(max_length=64, verbose_name="Email", blank=False)
    phone = models.CharField(max_length=64, verbose_name="Phone")
    notes = models.TextField(blank=True, verbose_name="Customer Notes")
