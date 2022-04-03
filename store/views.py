from django.shortcuts import get_object_or_404, render
from django.db.models import F

from .models import Category, Size, Product


def categories_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/category.html', {'category': category, 'products': products})

def products_all(request):
    products = Product.products.all()
    return render(request, 'store/home.html', {'products': products})

def product_info(request, slug):
    product = get_object_or_404(Product, 
                                slug=slug, 
                                in_stock=True
    )
    sizes = Size.objects.filter(
             product=product, in_stock=True
    )
    return render(request, 'store/product_info.html', {'product': product, 'sizes': sizes})
