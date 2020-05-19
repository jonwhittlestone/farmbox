from django.contrib import admin

from product.models import Product

class ProductAdmin(admin.ModelAdmin):

    list_display = ('sequence', 'name','code','pack_size','price','published', 'category')
    list_filter = ('category',)

    search_fields = ('name',)

    def has_add_permission(self, request):
        return False

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save'] = False
        return super(ProductAdmin, self).changeform_view(request, object_id, extra_context=extra_context)

admin.site.register(Product, ProductAdmin)
