from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse


# Create your views here.

def view_cart(request):
    '''A view to show shopping cart'''

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """Add an item to cart in the quantity submitted"""

    quantity = int(request.POST.get('qty'))
    redirect_url = request.POST.get('redirect_url')

    cart = request.session.get('cart', {})
    
    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity
    
    request.session['cart'] = cart
    return redirect(redirect_url)

def update_cart(request):
    """update an item qty in cart"""

    cart = request.session.get('cart')
    new_qty = int(request.POST.get('qty'))
    item_id = request.POST.get('item_id')
    print(f'Item Id: {item_id}')
    print(f'Qty: {new_qty}')

    cart[item_id] = new_qty

    request.session['cart'] = cart
    print(request.session['cart'])

    return redirect(reverse('view_cart'))

def add_single_item_to_cart(request, item_id):
    """Add an item to cart with quantity one"""
    
    quantity = 1

    cart = request.session.get('cart', {})
    
    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity
    
    request.session['cart'] = cart
    return redirect(reverse('products'))

def delete_an_item_from_cart(request, item_id):
    """Add an item to cart with quantity one"""

    cart = request.session.get('cart', {})
    
    cart.pop(item_id)
    
    request.session['cart'] = cart

    return redirect(reverse('view_cart'))

    
