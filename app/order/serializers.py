from rest_framework import serializers
from cart.cart import Cart
from .models import *
from cart_.views import cart_detail


class OrderSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        cart = Cart(request)
        order = Order.objects.create(author=request.user,  **validated_data)
        return order

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')
        products = cart_detail(request)
        representation['products'] = products
        return representation