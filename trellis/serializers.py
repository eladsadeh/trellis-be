
from rest_framework import serializers
from .models import Crop, Variety, Planting


class VarietySerializer(serializers.ModelSerializer):
    crop =  serializers.StringRelatedField(many=False, read_only=True)
    crop_id = serializers.PrimaryKeyRelatedField(queryset = Crop.objects.all(), source='crop')

    class Meta:
        model = Variety
        exclude = ['owner']


class CropSerializer(serializers.ModelSerializer):
    varieties = VarietySerializer(many=True, read_only=True)

    class Meta:
        model = Crop
        exclude = ['owner']
        depth = 1

class PlantingSerializer(serializers.ModelSerializer):
    variety = VarietySerializer(many=False, read_only=True)
    variety_id = serializers.PrimaryKeyRelatedField(queryset = Variety.objects.all(), source='variety')

    class Meta:
        model = Planting
        fields = '__all__' 