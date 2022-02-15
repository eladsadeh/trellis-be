from rest_framework import generics, permissions
# Create your views here.
from .models import Crop, Variety, Planting
# Import serializers
from .serializers import CropSerializer, VarietySerializer, PlantingSerializer
from trellis.permissions import IsOwner

# INDEX, POST
class CropList(generics.ListCreateAPIView):
    # queryset = Crop.objects.all()
    serializer_class = CropSerializer
    # permission_classes = [IsOwner]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        print(self.request.query_params)
        print(self.request.user)
        selected = self.request.query_params.get('selected')
        print(selected)

        if(selected == 'true'):
            queryset = Crop.objects.filter(selected = True, owner=self.request.user)
        else:
            queryset = Crop.objects.filter(owner=self.request.user)

        return queryset

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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class VarietyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Variety.objects.all()
    serializer_class = VarietySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PlantingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Planting.objects.all()
    serializer_class = PlantingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]