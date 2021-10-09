from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from django.contrib import admin
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from cart.views import CartViewSet

from product.views import *

schema_view = get_schema_view(
    openapi.Info(
        title="DordoiExpress-API",
        default_version='v1',
        description="API for DordoiExpress",
        terms_of_service="https://www.ourapp.com/policies/terms/",
        contact=openapi.Contact(email="contact@expenses.local"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


router = DefaultRouter()
router.register('comments', CommentViewSet)
router.register('products', ProductViewSet)
router.register('cart', CartViewSet)
router.register('categories', CategoryViewSet)
router.register('ratings', RatingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # swagger
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # mains
    path('', include(router.urls)),

    # swagger
    path('api/api.json/', schema_view.without_ui(cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # jwt авторизация
    path('account/', include('account.urls')),
]

# sudo systemctl restart nginx
# sudo systemctl restart gunicorn
# sudo systemctl daemon-reload
# sudo systemctl restart gunicorn
