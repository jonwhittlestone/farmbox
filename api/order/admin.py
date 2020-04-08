from django.contrib import admin

from order.models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name','customer_email','customer_phone','customer_postcode','fulfillment_method','customer_specified_fulfilled_at', 'created_at')

    search_fields = ('customer_name','customer_postcode', 'customer_email')
    list_filter = ('fulfillment_method',)

admin.site.register(Order, OrderAdmin)
