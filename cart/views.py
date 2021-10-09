from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .models import Cart
from .serializers import CartSerializer
from .permissions import IsAuthorPermission, IsCustomerPermission

MyUser = get_user_model()

class PermissionMixin:
    def get_permissions(self):
        if self.action == 'create':
            permissions = [IsCustomerPermission, ]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permissions = [IsAuthorPermission, ]
        else:
            permissions = []
        return [perm() for perm in permissions]

    def get_serializer_context(self):
        return {'request': self.request, 'action': self.action}


class CartViewSet(PermissionMixin, viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_queryset(self):
        if isinstance(self.request.user, MyUser):
            qs = self.request.user.profile_customer
            queryset = super().get_queryset()
            queryset = queryset.filter(user=qs)
            return queryset
        return None