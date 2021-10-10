from rest_framework import serializers

from .utils import get_rating
from .models import * 


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['photo']


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        comment = Comment.objects.create(author=request.user,  **validated_data)
        return comment


class ProductSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['rating'] = get_rating(representation.get('id'), Product)

        action = self.context.get('action')
        if action == 'retrieve':
            photos = PhotoSerializer(instance.photos.all(), many=True).data
            photos.append({"photo": "media/"+''.join(representation['main_photo'].split('media')[1:])})
            representation['photos'] = photos
            comments = CommentSerializer(instance.comments.all(), many=True).data
            representation['comments'] = comments
            representation.pop('main_photo')
        elif action == 'list':
            comments = CommentSerializer(instance.comments.all(), many=True).data
            if not comments:
                representation['comments'] = []
            else:
                representation['comments'] = comments[0]
        return representation

    def create(self, validated_data):
        request = self.context.get('request')
        images_data = request.FILES
        product = Product.objects.create(author=request.user, **validated_data)

        for photo in images_data.getlist('photos'):
            Photo.objects.create(photo=photo, product=product)
        return product

    def update(self, instance, validated_data):
        request = self.context.get('request')
        for key, value in validated_data.items():
            setattr(instance, key, value)
        images_data = request.FILES
        instance.images.all().delete()
        for photo in images_data.getlist('photos'):
            Photo.objects.create(photo=photo, product=instance)
        return instance


class RatingSerializer(serializers.ModelSerializer):
	author = serializers.ReadOnlyField(source='author.username')

	class Meta:
		model = Rating
		fields = '__all__'

	def create(self, validated_data):
		request = self.context.get('request')
		user = request.user
		product = validated_data.get('product')

		if Rating.objects.filter(author=user, product=product):
			rating = Rating.objects.get(author=user, product=product)
			return rating

		rating = Rating.objects.create(author=request.user, **validated_data)
		return rating