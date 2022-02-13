from rest_framework import serializers
from .models import Crop, Variety, Planting

class CropSerializer(serializers.ModelSerializer):

    class Meta:
        model = Crop
        fields = '__all__' 

class VarietySerializer(serializers.ModelSerializer):

    class Meta:
        model = Variety
        fields = '__all__'

class PlantingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Planting
        fields = '__all__' 