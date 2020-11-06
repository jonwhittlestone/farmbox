from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from product.models import Product


class ProductAdmin(SortableAdminMixin, admin.ModelAdmin):

    list_display = (
        "sequence",
        "_form_sequence",
        "name",
        "code",
        "price",
        "published",
    )
    list_filter = ("category", "published")
    list_display_links = ("name",)
    readonly_fields = ("code",)
    search_fields = ("name",)

    def has_add_permission(self, request):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

    def changeform_view(self, request, object_id=None, form_url="", extra_context=None):
        extra_context = extra_context or {}
        extra_context["show_save_and_continue"] = False
        extra_context["show_save"] = False
        return super(ProductAdmin, self).changeform_view(
            request, object_id, extra_context=extra_context
        )

    def _form_sequence(self, obj):
        if obj:
            return str(obj.sequence)


admin.site.register(Product, ProductAdmin)
