from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status

from product.serializers import *

from .permissions import *
from .models import *
from .serializers import *


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

	@action(detail=False, methods=['get'])
	def search(self, request, pk=None):
		q = request.query_params.get('q')
		queryset = self.get_queryset()
		queryset = queryset.filter(title__icontains=q)
		page = self.paginate_queryset(queryset)
		if page is not None:
			serializer = self.get_serializer(page, many=True)
			return self.get_paginated_response(serializer.data)
		serializer = ProductSerializer(queryset, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)


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