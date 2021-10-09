from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serializers import *
from .models import *


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer