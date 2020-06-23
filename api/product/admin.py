
# -*- coding: utf-8 -*-

from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

from product.models import Product

class ProductAdmin(SortableAdminMixin, admin.ModelAdmin):

    list_display = ('sequence', '_form_sequence', 'name','code','pack_size','price','published',)
    list_display_links = ('name', )

    list_filter = ('category',)

    readonly_fields = ('name','sequence','code', 'published')
    search_fields = ('name',)

    def _form_sequence(self, obj):
        if obj:
            return str(obj.sequence)

    def has_add_permission(self, request):
        return True

    def has_delete_permission(self, request, obj=None):
        return False

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save'] = False
        return super(ProductAdmin, self).changeform_view(request, object_id, extra_context=extra_context)

admin.site.register(Product, ProductAdmin)
