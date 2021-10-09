from rest_framework import serializers

from .models import *


class OrderSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        order = Order.objects.create(author=request.user,  **validated_data)
        return order