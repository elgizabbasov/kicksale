from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from store_cart.cart import Cart

@login_required
def CartView(request):
    cart = Cart(request)
    total = int(str(cart.get_total_cart_price()).replace('.', ''))
    return render(request, 'payment/landing.html')
