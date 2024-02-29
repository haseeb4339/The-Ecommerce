from django.contrib import admin

from .models import Product, Variation



class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug':('product_name',) }


class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variaton_category', 'variaton_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = list_display = ('product', 'variaton_category', 'variaton_value')





admin.site.register(Product,ProductAdmin)
admin.site.register(Variation, VariationAdmin)
