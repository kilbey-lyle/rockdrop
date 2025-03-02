from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import OrderForm
from django.conf import settings
from products.models import Product
import stripe

# Create your views here.
def create_checkout_session(request):

    cart = request.session.get('cart', {})
    line_items = []

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        name = product.name
        price = int(float(product.price)*100)
        stripe_dic = {
            'price_data': {
                'currency': 'gbp',
                'product_data': {'name': name,},
                'unit_amount': price,},
            'quantity': quantity,
        }
        line_items.append(stripe_dic)

    session = stripe.checkout.Session.create(
    line_items=line_items,
    mode='payment',
    success_url='http://127.0.0.1:8000/',
    cancel_url='http://localhost:4242/cancel',
    shipping_address_collection = {"allowed_countries": [ "GB", "IE"]},
    )

    return redirect(session.url, code=303)