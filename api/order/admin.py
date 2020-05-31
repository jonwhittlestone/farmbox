import os
from django.contrib import admin
from django.contrib.auth.models import User
from django.conf import settings
from order.models import Order, OrderForm, FulfillmentEvent, OrderFormFailure
from django.utils.safestring import mark_safe
from django.urls import reverse

class OrderFormAdmin(admin.ModelAdmin):
    list_display = ('filename', 'created_at', 'fulfillment_event', 'order')
    list_filter = ('fulfillment_event',)

    def has_add_permission(self, request):
        return False

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
    list_display = ('f_number', '_customer_sheet', 'customer_first_name', 'customer_last_name', 'customer_email', 'customer_phone',
                    'customer_postcode', 'fulfillment_event', 'fulfillment_method', 'created_at')
    search_fields = ('f_number', 'customer_first_name','customer_last_name','customer_postcode', 'customer_email')
    list_filter = ('fulfillment_event','fulfillment_method',)
    readonly_fields = ('f_number','_customer_sheet')
    inlines = (ProductQuantityInline,)
    exclude = ('collection_location',)


    def _customer_sheet(self,obj):
        if obj.id:
            url = reverse('download_customer_sheet',args=(obj.id,))
            return (mark_safe(f'<a href="{url}">View PDF</a>'))
        return ''
    def save_model(self, request, obj, form, change):
        obj.save()
        super(OrderAdmin, self).save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        obj.delete()
        obj.reassign_f_numbers()

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.delete()
        Order.reassign_future_f_numbers()


class FulfillmentEventAdmin(admin.ModelAdmin):

    list_display = ('id','target_date','_orders_count', '_input_sheet')
    readonly_fields = ('_orders_count','_input_sheet',)

    list_filter = ('id',)

    def _orders_count(self,obj):
        if obj:
            url = reverse('admin:order_order_changelist')
            # http://127.0.0.1:8000/admin/order/order/?fulfillment_event__id__exact=2
            # hacky. yep
            return (mark_safe(f'<a href="{url}?fulfillment_event__id__exact={obj.id}">{obj.orders_count}</a>'))
        return ''

    def _input_sheet(self,obj):
        if obj.id:
            url = reverse('download_input_xlsx',args=(obj.id,))
            return (mark_safe(f'<a href="{url}">Download</a>'))
        return ''



admin.site.register(OrderForm, OrderFormAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderFormFailure, OrderFormFailureAdmin)
admin.site.register(FulfillmentEvent, FulfillmentEventAdmin)
