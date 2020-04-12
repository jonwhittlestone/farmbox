from django.contrib import admin

from product.models import Product

class ProductAdmin(admin.ModelAdmin):

    list_display = ('name','slug','pack_size','price','published','sequence', 'category')
    list_filter = ('category',)

admin.site.register(Product, ProductAdmin)
