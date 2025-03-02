from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from checkout.models import Order, OrderLineItem
from django.conf import settings
from products.models import Product
from cart.contexts import cart_contents
import json
import stripe

# Create your views here.
def create_checkout_session(request):

    cart = request.session.get('cart', {})
    line_items = []


    if not settings.STRIPE_SECRET_KEY:
        messages.error(request, 'No stripe secret, have you set in your env?')
    
    stripe.api_key = settings.STRIPE_SECRET_KEY

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
    
    cart_content = cart_contents(request)
    if cart_content['delivery'] > 0:
        session = stripe.checkout.Session.create(
        line_items=line_items,
        mode='payment',
        success_url='http://127.0.0.1:8000/checkout/checkout_success/?session_id={CHECKOUT_SESSION_ID}',
        cancel_url='http://127.0.0.1:8000/',
        shipping_address_collection = {"allowed_countries": [ "GB", "IE"]},
        phone_number_collection = {"enabled": True},
        shipping_options=[
            {
                "shipping_rate_data": {
                    "type": "fixed_amount",
                    "fixed_amount": {"amount": 1500, "currency": "gbp"},
                    "display_name": "Standard Delivery",
                }
            }
        ]
        )
    else:
        session = stripe.checkout.Session.create(
        line_items=line_items,
        mode='payment',
        success_url='http://127.0.0.1:8000/checkout/checkout_success/?session_id={CHECKOUT_SESSION_ID}',
        cancel_url='http://127.0.0.1:8000/',
        shipping_address_collection = {"allowed_countries": [ "GB", "IE"]},
        phone_number_collection = {"enabled": True}
        )

    stripe.checkout.Session.modify( 
        session.id,
        metadata={"cart_contents": json.dumps(cart)},
    )

    del request.session['cart']

    return redirect(session.url, code=303)

def checkout_success(request):
    session_id = request.GET.get('session_id')
    session = stripe.checkout.Session.retrieve(session_id)

    shipping_info = session.shipping_details


    order = Order(
        full_name = session.customer_details.name,
        email = session.customer_details.email,
        phone_number = session.customer_details.phone,
        street_address1 = session.shipping_details.address.line1,
        street_address2 = session.shipping_details.address.line2,
        town_or_city = session.shipping_details.address.city,
        postcode = session.shipping_details.address.postal_code, 
        country = session.shipping_details.address.country,
        county = session.shipping_details.address.state,
    )
    order.save()

    cart = json.loads(session.metadata.cart_contents)


    for item_id, quantity in cart.items():
        product = Product.objects.get(id=item_id)
        order_line_item = OrderLineItem(
            order=order,
            product=product,
            quantity=quantity
        )
        order_line_item.save()

    context = {
        'shipping_info': shipping_info,
        'order' : order
    }

    return render(request, 'checkout/checkout_success.html', context)