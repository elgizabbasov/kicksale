from django.contrib import admin

from .models import Category, Size, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'brand', 'condition', 'price', 
                    'in_stock', 'created', 'updated']
    list_filter = ['in_stock']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['prod_size', 'in_stock', 'product', 'quantity', 'created']
    list_filter = ['in_stock']
    list_editable = ['in_stock', 'quantity']
