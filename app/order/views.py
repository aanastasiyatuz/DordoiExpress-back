from django.shortcuts import render
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .permissions import *
from .serializers import *
from .models import *


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_permissions(self):
        if self.action in ['destroy']:
            permissions = [IsOrderAuthor]
        elif self.action in ['create']:
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAdminUser]
        return [permission() for permission in permissions]