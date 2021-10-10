from django.contrib import admin
from .models import ProfileSeller, ProfileClient

admin.site.register(ProfileSeller)
admin.site.register(ProfileClient)