from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from product.serializers import *

from .models import *
from .serializers import *


# Create your views here.
class CommentViewSet(ModelViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer

class ProductViewSet(ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer