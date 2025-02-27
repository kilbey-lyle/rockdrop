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
        'is_public'
    )

    ordering = ('-is_public', 'price')

admin.site.register(Product, ProductAdmin)