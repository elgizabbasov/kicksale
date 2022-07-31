from django.shortcuts import get_object_or_404, render

from .models import Category, Size, Product


def categories_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category__in=Category.objects.get(slug=category_slug).get_descendants(include_self=True))
    return render(request, 'store/category.html', {'category': category, 'products': products})

def products_all(request):
    products = Product.objects.prefetch_related("product_image").filter(in_stock=True)
    return render(request, 'store/home.html', {'products': products})

def product_info(request, slug):
    product = get_object_or_404(Product, 
                                slug=slug, 
                                in_stock=True
    )
    sizes = Size.objects.filter(
             product=product, in_stock=True
    )
    quantities = {}
    for i in sizes:
        for j in range(i.quantity):
            quantities[i] = j
            
        
    return render(request, 'store/product_info.html', {'product': product, 'sizes': sizes, 'quantities': quantities})

def about_info(request):
    return render(request, 'store/about_info.html')
