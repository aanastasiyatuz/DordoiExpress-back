from rest_framework import serializers
from cart.cart import Cart
from .models import *


class OrderSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        cart = Cart(request)
        order = Order.objects.create(author=request.user,  **validated_data)
        print(cart.cart.items())
        for product in cart.cart.items():
            order.products.append(product)
        return order