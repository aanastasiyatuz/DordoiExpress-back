from rest_framework.response import Response
from product.models import Product
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.http import JsonResponse

@login_required(login_url="/account/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return JsonResponse(cart.cart)


@login_required(login_url="/account/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return JsonResponse(cart.cart)


@login_required(login_url="/account/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return JsonResponse(cart.cart)


@login_required(login_url="/account/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    if cart.cart.items().get(str(product.id)) == 1:
        cart.remove(product)
    else:
        cart.decrement(product=product)
    return JsonResponse(cart.cart)


@login_required(login_url="/account/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return Response("Succesfully cleared a cart", status=200)


@login_required(login_url="/account/login")
def cart_detail(request):
    cart = Cart(request)
    return JsonResponse(cart.cart)