from django.shortcuts import render
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from product.serializers import *

from .permissions import *
from .models import *
from .serializers import *


# Create your views here.
class CommentViewSet(ModelViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['action'] = self.action
        return context

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class RatingViewSet(ModelViewSet):
	queryset = Rating.objects.all()
	serializer_class = RatingSerializer

	def get_permissions(self):
		if self.action in ['update', 'partial_update', 'destroy']:
			permissions = [IsProductAuthor]
		elif self.action in ['create']:
			permissions = [IsAuthenticated]
		else:
			permissions = [IsAdminUser]
		return [permission() for permission in permissions]