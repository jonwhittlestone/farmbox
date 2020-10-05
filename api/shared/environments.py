import re
import random
from django.forms import ValidationError
from django.conf import settings
from django.utils import timezone
from order.models import Order, FulfillmentEvent, OrderForm, OrderFormFailure
from product.models import Product
from customer.models import Customer
from order.fixtures import sample_fulfillment_events, sample_orders
from product.fixtures import initial_products


def create_sample_orders():

    for evt in sample_fulfillment_events:
        new_evt = FulfillmentEvent(**evt)
        new_evt.save()

    for order in sample_orders:

        customer = Customer.objects.create(
            first_name=order.get("customer_first_name"),
            last_name=order.get("customer_last_name"),
            address=order.get("customer_address"),
            postcode=order.get("customer_postcode"),
            email=order.get("customer_email"),
            phone=order.get("customer_phone"),
        )

        order["user_id"] = 1
        order["customer_id"] = customer.id
        order["fulfillment_event_id"] = new_evt.id
        ord = Order(**order)
        try:
            ord.full_clean()
        except ValidationError as e:
            print("")
            print(f"THE MODEL INSTANCE DID NOT PASS VALIDATION. SKIPPING .. {e}")
            print("")
            pass
        ord.save()

    # add sample products
    for ord in Order.objects.all():
        valid_products_ids = Product.objects.all().values_list("id", flat=True)
        ids = list(valid_products_ids)
        random_products_ids = random.sample(
            ids, min(len(ids), settings.NUMBER_PRODUCTS_TO_ADD_TO_A_SAMPLE_ORDER)
        )

        qs = Product.objects.filter(id__in=random_products_ids)
        for p in qs:
            from order.models import ProductQuantity

            ProductQuantity.objects.create(
                order=ord, product=p, quantity=random.randint(1, 3)
            )


def create_product_fixtures():
    for product in initial_products:
        try:
            p = Product(**product)
            p.code = re.findall("[A-Z]{2}[0-9]*$", p.name)[0]
            p.save()
        except Exception:
            print(p.code)


class FactoryReset:
    def run(self):
        self.remove_orders()
        self.remove_forms()
        self.remove_events()
        self.remove_products()
        self.provision_products()
        self.provision_orders()

    def provision_products(self):
        create_product_fixtures()

    def provision_orders(self):
        create_sample_orders()

    def remove_products(self):
        Product.objects.all().delete()

    def remove_forms(self):
        OrderForm.objects.all().delete()
        OrderFormFailure.objects.all().delete()

    def remove_orders(self):
        Order.objects.all().delete()

    def remove_events(self):
        FulfillmentEvent.objects.all().delete()
