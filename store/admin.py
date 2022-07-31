from django.contrib import admin

from mptt.admin import MPTTModelAdmin

from .models import (Category, 
                     Size, 
                     Product,
                     ProductImage,)


admin.site.register(Category, MPTTModelAdmin)


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['prod_size', 'in_stock', 'product', 'quantity', 'created']
    list_filter = ['in_stock']
    list_editable = ['in_stock', 'quantity']
    

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline,
    ]
    list_display = ['title', 'slug', 'brand', 'condition', 'price', 
                    'in_stock', 'created', 'updated']
    list_filter = ['in_stock']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('title',)}