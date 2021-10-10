from django.urls import path
from .views import *

urlpatterns = [
    path('seller/', ProfileSellerListView.as_view()),
    path('seller/<int:pk>/', ProfileSellerDetailView.as_view()),
    path('seller-update/<int:pk>/', ProfileSellerUpdateView.as_view()),
    path('client/', ProfileClientListView.as_view()),
    path('client/<int:pk>/', ProfileClientDetailView.as_view()),
    path('client-update/<int:pk>/', ProfileClientUpdateView.as_view()),
]