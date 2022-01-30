from django.shortcuts import get_object_or_404, render
from django.db.models import F

from .models import Category, Size, Product

################################################################
# TODO: Now in your views check whether a product_size is available for the given product or not. 
# If product_size is not there do a create or else update the quantity.
################################################################


def categories_all(request):
    return {
        'categories': Category.objects.all()
    }

def products_all(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

def product_info(request, slug):
    product = get_object_or_404(Product, 
                                slug=slug, 
                                in_stock=True
    )
    sizes = Size.objects.filter(
             product=product, in_stock=True
    )
    return render(request, 
                  'store/product_info.html', 
                  {'product': product, 'sizes': sizes
        }
    )
    

