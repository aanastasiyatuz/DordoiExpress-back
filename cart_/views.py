from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from product.models import Product
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

@login_required(login_url="/account/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return cart.items()


@login_required(login_url="/account/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return cart.items()


@login_required(login_url="/account/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return cart.items()


@login_required(login_url="/account/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    if cart.items().get(str(product.id)) == 1:
        cart.remove(product)
    else:
        cart.decrement(product=product)
    return cart.items()


@login_required(login_url="/account/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return HttpResponse("Succesfully cleared a cart", status_code=200)


@login_required(login_url="/account/login")
def cart_detail(request):
    cart = Cart(request)
    return cart.items()