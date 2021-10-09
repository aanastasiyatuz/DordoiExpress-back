from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.db import models

User = get_user_model()


STATUS_CHOICES = (
    ('in stock', "В наличии"),
    ('out of stock', "Нет в наличии"),
    ('awaiting', "В ожидании")
)


class Category(models.Model):
	slug = models.SlugField(max_length=100, primary_key=True)
	title = models.CharField(max_length=100, unique=True)

	class Meta:
		ordering = ['slug']

	def __str__(self):
		return self.title


class Photo(models.Model):
    photo = models.ImageField(upload_to='product_photos', blank=True, null=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='photos')


class Product(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.PositiveIntegerField(default=0)
    amount = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    main_photo = models.ImageField(upload_to='product_photos')

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title


class Rating(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')
	rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)])

	class Meta:
		ordering = ['id']

	def __str__(self):
		return f'{self.author}: {self.pin} - {self.rating}'


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    photo = models.ImageField(upload_to='comment_photos', blank=True, null=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.author.username