from django.urls import path
from .views import *

urlpatterns = [
    path('', cart_detail),
    path('add/<int:id>/', cart_add),
    path('item_increment/<int:id>/', item_increment),
    path('item_decrement/<int:id>/', item_decrement),
    path('item_clear/<int:id>/', item_clear),
    path('clear/', cart_clear),
]