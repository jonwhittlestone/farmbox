from django.contrib import admin
from django.conf import settings
from order.models import Order, OrderForm, FulfillmentEvent
from django.utils.safestring import mark_safe
from django.urls import reverse

class OrderFormAdmin(admin.ModelAdmin):
    list_display = ('filename', 'created_at', 'fulfillment_event', 'order_created')

    list_filter = ('fulfillment_event',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name','customer_email','customer_phone','customer_postcode','fulfillment_event','fulfillment_method', 'created_at')

    search_fields = ('customer_name','customer_postcode', 'customer_email')
    list_filter = ('fulfillment_event','fulfillment_method',)


class FulfillmentEventAdmin(admin.ModelAdmin):

    list_display = ('id','target_date','orders_count', '_input_sheet')
    readonly_fields = ('orders_count','_input_sheet',)

    def _input_sheet(self,obj):
        # print(obj.id)
        url = reverse('download_input_xlsx',args=(obj.id,))
        return (mark_safe(f'<a href="{url}">Download</a>'))



admin.site.register(OrderForm, OrderFormAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(FulfillmentEvent, FulfillmentEventAdmin)
