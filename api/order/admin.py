import os
from django.contrib import admin
from django.conf import settings
from order.models import Order, OrderForm, FulfillmentEvent, OrderFormFailure
from django.utils.safestring import mark_safe
from django.urls import reverse

class OrderFormAdmin(admin.ModelAdmin):
    list_display = ('filename', 'created_at', 'fulfillment_event', 'order')

    list_filter = ('fulfillment_event',)

class OrderFormFailureAdmin(admin.ModelAdmin):
    list_display = ('id', '_form_created_at', 'reason', '_show_form')

    exclude=('reason','form')
    readonly_fields=('reason', 'form')

    def _show_form(self, obj):
        if obj:
            url = reverse('admin:order_orderform_changelist')
            return (mark_safe(f'<a href="{url}">{os.path.basename(obj.form.filename)}</a>'))

    def _form_created_at(self, obj):
        if obj:
            return obj.form.created_at


    # _show_form.short_description = "Form"
    def has_add_permission(self, request):
        return False

# from django.db.models.loading import get_model
# OrderQuantityMdl = get_model('order', 'OrderQuantity')
# from order.models import OrderQuantity
class ProductQuantityInline(admin.TabularInline):
    from order.models import ProductQuantity
    model = ProductQuantity
    extra=1

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_email', 'customer_phone',
                    'customer_postcode', 'fulfillment_event', 'fulfillment_method', 'created_at')

    search_fields = ('customer_name','customer_postcode', 'customer_email')
    list_filter = ('fulfillment_event','fulfillment_method',)
    inlines = (ProductQuantityInline,)


class FulfillmentEventAdmin(admin.ModelAdmin):

    list_display = ('id','target_date','orders_count', '_input_sheet')
    readonly_fields = ('orders_count','_input_sheet',)

    list_filter = ('id',)

    def _input_sheet(self,obj):
        if obj:
            url = reverse('download_input_xlsx',args=(obj.id,))
            return (mark_safe(f'<a href="{url}">Download</a>'))
        return ''



admin.site.register(OrderForm, OrderFormAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderFormFailure, OrderFormFailureAdmin)
admin.site.register(FulfillmentEvent, FulfillmentEventAdmin)
