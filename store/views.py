from django.http import JsonResponse
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
        
    return render(request, 'store/product_info.html', {'product': product, 'sizes': sizes})

def get_quantities(request):
    size = request.GET.get('size')
    quantities = list(Size.objects.filter(prod_size=size).values("quantity"))
    response_data = {
        "quantities": quantities
    }
    return JsonResponse(response_data)

def about_info(request):
    return render(request, 'store/about_info.html')
