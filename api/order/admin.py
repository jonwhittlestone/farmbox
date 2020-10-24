import os
import datetime
from django.contrib import admin
from django.utils.translation import ngettext
from django.contrib import messages
from django.contrib.auth.models import User
from django.conf import settings
from order.models import (
    Order,
    OrderForm,
    FulfillmentEvent,
    OrderFormFailure,
    ProductQuantity,
)
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.shortcuts import render, redirect


class OrderFormAdmin(admin.ModelAdmin):
    list_display = ("filename", "created_at", "fulfillment_event", "order")
    list_filter = ("fulfillment_event",)

    def has_add_permission(self, request):
        return False


class OrderFormFailureAdmin(admin.ModelAdmin):
    list_display = ("id", "_form_created_at", "reason", "_show_form")

    exclude = ("reason", "form")
    readonly_fields = ("reason", "form")

    def _show_form(self, obj):
        if obj:
            url = reverse("admin:order_orderform_changelist")
            return mark_safe(
                f'<a href="{url}">{os.path.basename(obj.form.filename)}</a>'
            )

    def _form_created_at(self, obj):
        if obj:
            return obj.form.created_at

    def has_add_permission(self, request):
        return False


# from django.db.models.loading import get_model
# OrderQuantityMdl = get_model('order', 'OrderQuantity')
# from order.models import OrderQuantity
class ProductQuantityInline(admin.TabularInline):
    model = ProductQuantity
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "f_number",
        "created_at",
        "_repeated_order_original",
        "_customer_sheet_pdf",
        "customer_first_name",
        "customer_last_name",
        "customer_email",
        "customer_phone",
        "customer_postcode",
        "fulfillment_event",
        "fulfillment_method",
    )
    search_fields = (
        "f_number",
        "customer_first_name",
        "customer_last_name",
        "customer_postcode",
        "customer_email",
    )
    list_filter = (
        "fulfillment_event",
        "fulfillment_method",
        "created_at",
        "customer_id",
    )
    readonly_fields = (
        "created_at",
        "customer_first_name",
        "customer_last_name",
        "customer_address",
        "customer_postcode",
        "customer_email",
        "customer_phone",
        "f_number",
        "_customer_sheet_pdf",
        "_repeated_order_original",
    )
    fields = (
        "f_number",
        "created_at",
        "_repeated_order_original",
        "customer_first_name",
        "customer_last_name",
        "customer_address",
        "customer_postcode",
        "customer_email",
        "customer_phone",
        "fulfillment_method",
        "fulfillment_event",
        "notes",
        "_customer_sheet_pdf",
    )

    inlines = (ProductQuantityInline,)
    exclude = ("collection_location", "repeated_order_original")
    actions = ["make_repeat_order"]
    change_list_template = "admin/order/order/change_list.html"

    def make_repeat_order(self, request, queryset):
        """
        Duplicates orders
        Reassigns f-numbers
        """

        if "apply" in request.POST:
            # in: 01/08/2020  # required:  YYYY-MM-DD
            event_date = request.POST.get("f_event_target_date")
            fmt_event_date = datetime.datetime.strptime(event_date, "%d/%m/%Y")
            f_event_obj, created = FulfillmentEvent.objects.get_or_create(
                target_date=fmt_event_date
            )
            for count, obj in enumerate(queryset):
                original_pk = obj.pk
                original_products_quantities = obj.product_quantities.all()

                obj.pk = None
                obj.fulfillment_event = f_event_obj
                obj.repeated_order_original = Order.objects.get(id=original_pk)
                obj.save()

                for prod_qty in original_products_quantities:
                    prod_qty.pk = None
                    prod_qty.order_id = obj.pk
                    prod_qty.save()

            messages.add_message(
                request,
                messages.SUCCESS,
                f"{count + 1} order(s) duplicated as a repeat order for event {f_event_obj}",
            )
            url = reverse("admin:order_order_changelist")
            return redirect(url)

        return render(
            request, "admin/order/order/duplicate.html", context={"orders": queryset}
        )

    make_repeat_order.short_description = "Repeat order(s) to new event"

    def has_add_permission(self, request):
        return False

    def _repeated_order_original(self, obj):
        if obj.id and obj.repeated_order_original:
            url = reverse(
                "admin:order_order_change", args=(obj.repeated_order_original.id,)
            )
            return mark_safe(f'<a href="{url}">{obj.repeated_order_original}</a>')
        return ""

    def _customer_sheet_pdf(self, obj):
        if obj.id:
            url = reverse("download_customer_sheet_pdf", args=(obj.id,))
            return mark_safe(f'<a href="{url}">View</a>')
        return ""

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

    list_display = (
        "id",
        "target_date",
        "_orders_count",
        "_input_sheet",
        "_customer_sheets_pdf",
        "_customer_sheets_xlsx",
    )
    readonly_fields = (
        "_orders_count",
        "_input_sheet",
        "_customer_sheets_pdf",
        "_customer_sheets_xlsx",
    )

    list_filter = ("id",)

    def _orders_count(self, obj):
        if obj:
            url = reverse("admin:order_order_changelist")
            # http://127.0.0.1:8000/admin/order/order/?fulfillment_event__id__exact=2
            # hacky. yep
            return mark_safe(
                f'<a href="{url}?fulfillment_event__id__exact={obj.id}">{obj.orders_count}</a>'
            )
        return ""

    def _customer_sheets_pdf(self, obj):
        if obj.id:
            url = reverse("download_event_customer_sheet_pdf", args=(obj.id,))
            return mark_safe(f'<a href="{url}">View</a>')
        return ""

    def _customer_sheets_xlsx(self, obj):
        if obj.id:
            url = reverse("download_event_customer_sheet_xlsx", args=(obj.id,))
            return mark_safe(f'<a href="{url}">Download</a>')
        return ""

    def _input_sheet(self, obj):
        if obj.id:
            url = reverse("download_input_xlsx", args=(obj.id,))
            return mark_safe(f'<a href="{url}">Download</a>')
        return ""


admin.site.register(OrderForm, OrderFormAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderFormFailure, OrderFormFailureAdmin)
admin.site.register(FulfillmentEvent, FulfillmentEventAdmin)
