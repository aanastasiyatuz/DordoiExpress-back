from rest_framework import serializers

from .utils import get_rating
from .models import * 


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
	author = serializers.ReadOnlyField(source='author.username')
	created = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%S', read_only=True)

	class Meta:
		model = Product
		fields = '__all__'

	def to_representation(self, instance):
		representation = super().to_representation(instance)
		action = self.context.get('action')
		representation['rating'] = get_rating(representation.get('id'), Product)

		if action == 'list':
			representation.pop('de')
			representation.pop('link')
			representation['comments'] = instance.comments.count()
		elif action == 'retrieve':
			representation['comments'] = CommentSerializer(instance.comments.all(), many=True).data
			queryset = Product.objects.exclude(id=instance.id).filter(category=instance.category)[:4]
			representation['similar'] = ProductSerializer(queryset, many=True).data

		return representation

	def create(self, validated_data):
		request = self.context.get('request')
		Product = Product.objects.create(author=request.user, **validated_data)
		user = CustomUser.objects.get(id=request.user.id)

		for follower in Product.author.profile.followers.all():
			send_notification(Product.author, follower, Product)

		return Product