from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })


    if total < settings.FREE_DELIVERY_MIN:
        delivery = settings.STANDARD_DELIVERY_CHARGE
        free_delivery_left_to_spend = settings.FREE_DELIVERY_MIN - total
    else:
        delivery = 0
        free_delivery_left_to_spend = 0
    
    grand_total = delivery + total

    context = {
        'cart_items' : cart_items,
        'total' : total,
        'product_count': product_count,
        'delivery' : delivery,
        'free_delivery_left_to_spend' : free_delivery_left_to_spend,
        'grand_total' : grand_total,
        'free_delivery_min' : settings.FREE_DELIVERY_MIN,
    }

    return context