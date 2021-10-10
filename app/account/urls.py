from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import RegistrationView, ActivationView, ForgotPassword, ForgotPasswordComplete

urlpatterns = [
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegistrationView.as_view()),
    path('activate/<str:activation_code>/', ActivationView.as_view()),
    path('forgot-password/', ForgotPassword.as_view()),
    path('forgot-password-complete/<str:activation_code>/', ForgotPasswordComplete.as_view()),
]