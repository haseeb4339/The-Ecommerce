from django.shortcuts import render
from store.models import Product
from carts.models import Cart, CartItem



def _cart_add(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id = _cart_add(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_add(request)
        )
    cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity +=1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart,

        )
        cart_item.save()


def cart(request):

    return render(request, 'store/cart.html')
