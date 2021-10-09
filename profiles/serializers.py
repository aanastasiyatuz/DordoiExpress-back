from rest_framework import serializers
from .models import ProfileSeller, ProfileClient


class ProfileSellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileSeller
        fields = '__all__'


class ProfileClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileClient
        fields = '__all__'