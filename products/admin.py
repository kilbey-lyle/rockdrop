from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
        'stone_type',
        'metal_type',
        'chain_length',
        'chain_thickness',
        'is_public',
        'has_sizes',
    )

    ordering = ('-is_public', 'price')

admin.site.register(Product, ProductAdmin)