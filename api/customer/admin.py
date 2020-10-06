from .models import Customer
from order.models import Order
from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "postcode", "_orders_count")

    search_fields = (
        "first_name",
        "last_name",
        "email",
        "postcode",
    )

    def _orders_count(self, obj):
        if obj:
            customer_orders = Order.objects.filter(customer=obj)
            if customer_orders:
                url = reverse("admin:order_order_changelist")
                # http://127.0.0.1:8000/admin/order/order/?fulfillment_event__id__exact=2
                return mark_safe(
                    f'<a href="{url}?customer_id__id__exact={obj.id}">{customer_orders.count()}</a>'
                )
            else:
                return ""
        return ""


admin.site.register(Customer, CustomerAdmin)
