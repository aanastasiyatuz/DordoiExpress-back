from rest_framework import generics
from .models import ProfileSeller, ProfileClient
from .serializers import ProfileSellerSerializer, ProfileClientSerializer



class ProfileSellerListView(generics.ListAPIView):
    queryset = ProfileSeller.objects.all()
    serializer_class = ProfileSellerSerializer

class ProfileSellerDetailView(generics.RetrieveAPIView):
    queryset = ProfileSeller.objects.all()
    serializer_class = ProfileSellerSerializer

class ProfileSellerUpdateView(generics.UpdateAPIView):
    queryset = ProfileSeller.objects.all()
    serializer_class = ProfileSellerSerializer



class ProfileClientListView(generics.ListAPIView):
    queryset = ProfileClient.objects.all()
    serializer_class = ProfileClientSerializer

class ProfileClientDetailView(generics.RetrieveAPIView):
    queryset = ProfileClient.objects.all()
    serializer_class = ProfileClientSerializer

class ProfileClientUpdateView(generics.UpdateAPIView):
    queryset = ProfileClient.objects.all()
    serializer_class = ProfileClientSerializer

