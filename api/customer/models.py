from django.db import models


def get_or_create_customer(order_details):
    qs = Customer.objects.filter(email=order_details.get("customer_email"))
    if qs:
        return qs[0]

    order = order_details
    return Customer.objects.create(
        first_name=order.get("customer_first_name"),
        last_name=order.get("customer_last_name"),
        address=order.get("customer_address"),
        postcode=order.get("customer_postcode"),
        email=order.get("customer_email"),
        phone=order.get("customer_phone"),
    )


# Create your models here.
class Customer(models.Model):

    first_name = models.CharField(
        max_length=512, verbose_name="First Name", blank=False
    )
    last_name = models.CharField(max_length=512, verbose_name="Last Name", blank=False)
    address = models.CharField(
        max_length=512, verbose_name="Address", blank=False, db_index=True
    )
    postcode = models.CharField(max_length=8, verbose_name="Postcode", blank=False)
    email = models.EmailField(
        max_length=64, verbose_name="Email", blank=False, db_index=True
    )
    phone = models.CharField(max_length=64, verbose_name="Phone")
    notes = models.TextField(blank=True, verbose_name="Customer Notes")

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.name}"
