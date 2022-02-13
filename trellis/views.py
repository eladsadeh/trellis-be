from rest_framework import generics, permissions
# Create your views here.
from .models import Crop, Variety, Planting
# Import serializers
from .serializers import CropSerializer, VarietySerializer, PlantingSerializer
from trellis.permissions import IsOwner

# INDEX, POST
class CropList(generics.ListCreateAPIView):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class VarietyList(generics.ListCreateAPIView):
    queryset = Variety.objects.all()
    serializer_class = VarietySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PlantingList(generics.ListCreateAPIView):
    queryset = Planting.objects.all()
    serializer_class = PlantingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# SHOW, PUT, DELETE for all models
class CropDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer
    permission_classes = [permissions.IsAuthenticated]

class VarietyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Variety.objects.all()
    serializer_class = VarietySerializer
    permission_classes = [permissions.IsAuthenticated]

class PlantingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Planting.objects.all()
    serializer_class = PlantingSerializer
    permission_classes = [permissions.IsAuthenticated]