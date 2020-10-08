import logging
from django.core.management.base import BaseCommand
from customer.models import Customer
from order.models import Order

logger = logging.getLogger(__name__)


def create_customers_from_orders():
    qs = Order.objects.all().exclude(customer__isnull=False)
    for order in qs:
        cust = Customer.objects.filter(email=order.customer_email)
        if cust:
            order.customer_id = cust[0].id
            order.save()
            continue

        d_order = order.__dict__
        new_customer = Customer.objects.create(
            first_name=d_order.get("customer_first_name"),
            last_name=d_order.get("customer_last_name"),
            address=d_order.get("customer_address"),
            postcode=d_order.get("customer_postcode"),
            email=d_order.get("customer_email"),
            phone=d_order.get("customer_phone"),
        )

        order.customer_id = new_customer.id
        order.save()


class Command(BaseCommand):
    def handle(self, *args, **options):
        logger.info("CALLED: create_customers_from_orders")
        create_customers_from_orders()
        self.stdout.write(
            self.style.SUCCESS("\ncreate_customers_from_orders Completed.")
        )
