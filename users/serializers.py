from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import User
# from trellis.serializers import CropSerializer, VarietySerializer, PlantingSerializer

class UserCreateSerializer(UserCreateSerializer):
 
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email')

class UserSerializer(UserSerializer):

    class Meta:
        model: User
        fields: ('id')