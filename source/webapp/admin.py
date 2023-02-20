from django.contrib import admin
from webapp.models import Product, Category


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'description',
                    'category', 'price', 'created_at', 'image_url')
    list_filter = ('id', 'product_name', 'category', 'price', 'created_at')
    search_fields = ('product_name', 'category')
    fields = ('product_name', 'description', 'category', 'price', 'image_url')
    readonly_fields = 'id', 'created_at'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'description')
    list_filter = ('id', 'category_name')
    search_fields = ('category_name', 'description')
    fields = ('category_name', 'description')
    readonly_fields = 'id', 'id'


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
