from django.contrib import admin

from order.models import Order
from order.models import FulfillmentEvent
from django.utils.safestring import mark_safe

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name','customer_email','customer_phone','customer_postcode','fulfillment_event','fulfillment_method', 'created_at')

    search_fields = ('customer_name','customer_postcode', 'customer_email')
    list_filter = ('fulfillment_event','fulfillment_method',)


class FulfillmentEventAdmin(admin.ModelAdmin):
    list_display = ('id','target_date', '_input_sheet')
    readonly_fields = ('_input_sheet',)

    def _input_sheet(self,obj):
        # print(obj.id)
        return (mark_safe('<a href="">Download</a>'))


admin.site.register(Order, OrderAdmin)

admin.site.register(FulfillmentEvent, FulfillmentEventAdmin)
