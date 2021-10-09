from django.contrib.auth import get_user_model
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


MyUser = get_user_model()


class ProfileSeller(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name='profile_seller')
    email = models.EmailField(max_length=100, unique=True)
    bio = models.TextField(max_length=300, default='no bio...')
    avatar = models.ImageField(upload_to='avatars/', default='default-avatar.jpg')
    country = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    phone = PhoneNumberField(blank=True)

    def __str__(self):
        return f'{self.user.email}'


class ProfileClient(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name='profile_client')
    email = models.EmailField(max_length=100, unique=True)
    avatar = models.ImageField(upload_to='avatars/', default='default-avatar.jpg')
    country = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    phone = PhoneNumberField(blank=True)

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.email
