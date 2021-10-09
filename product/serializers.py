from rest_framework import serializers

from .utils import get_rating
from .models import * 


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields ='__all__'

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
# 	created = serializers.DateTimeField(format='%d/%m/%Y %H:%M:%S', read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # representation['photos'] = PhotoSerializer(instance.photos.all(), many=True).data
        photos = [photo for photo in instance.photos.all()]


        action = self.context.get('action')
        # if action == 'list':
        #     representation['main_photo'] += PhotoSerializer(instance.photos.all(), many=True).data
        # elif action == 'retrieve':
        #     representation['replies'] = ReplySerializer(instance.replies.all(), many=True).data
        return representation

    def create(self, validated_data):
        request = self.context.get('request')
        images_data = request.FILES
        product = Product.objects.create(author=request.user, **validated_data)

        for image in images_data.getlist('photos'):
            Photo.objects.create(image=image, product=product)
        return product

    # def update(self, instance, validated_data):
    #     request = self.context.get('request')
    #     for key, value in validated_data.items():
    #         setattr(instance, key, value)
    #     images_data = request.FILES
    #     instance.images.all().delete()
    #     for image in images_data.getlist('images'):
    #         CodeImage.objects.create(image=image, problem=instance)
    #     return instance