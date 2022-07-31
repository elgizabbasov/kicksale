import json
import os
import stripe

from django.shortcuts import render
from django.conf import settings
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from store_cart.cart import Cart
from orders.views import payment_confirmation

@login_required
def CartView(request):
    cart = Cart(request)
    total = int(str(cart.get_total_cart_price()).replace('.', '')) # Stripe intent needs int
    
    stripe.api_key = settings.STRIPE_SECRET_KEY
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency='cad',
        metadata={'userid': request.user.id}
    )
    
    return render(request, 'payment/landing.html', {'client_secret': intent.client_secret, 'STRIPE_PUBLISHABLE_KEY': os.environ.get('STRIPE_PUBLISHABLE_KEY')})

@csrf_exempt
def stripe_webhook(request):
    """ If payment succesful, mark billing status as completed
    """
    payload = request.body
    event = None
    
    try:
        event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key
        )
    except ValueError as e:
        print(e)
        return HttpResponse(status=400)
    
    if event.type == 'payment_intent.succeeded':
        payment_confirmation(event.data.object.client_secret)
    else:
        print(f'Unhandled event type {event.type}')
        
    return HttpResponse(status=200)
        
def order_placed(request):
    cart = Cart(request)
    cart.clear()
    return render(request, 'payment/orderplaced.html')
