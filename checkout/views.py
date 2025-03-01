from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import OrderForm
from django.conf import settings
from products.models import Product
import stripe

# Create your views here.

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)


def create_checkout_session(request):

    print(settings.STRIPE_SECRET_KEY)
    stripe.api_key = settings.STRIPE_SECRET_KEY

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
    success_url='http://localhost:4242/success',
    cancel_url='http://localhost:4242/cancel',
    shipping_address_collection = {"allowed_countries": [ "GB", "IE"]},
    )

    return redirect(session.url, code=303)