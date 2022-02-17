
from rest_framework import serializers
from .models import Crop, Variety, Planting
from users.models import User
from users.serializers import UserSerializer


class VarietyShallowSerializer(serializers.ModelSerializer):
    crop_id = serializers.PrimaryKeyRelatedField(queryset = Crop.objects.all(), source='crop')

    class Meta:
        model = Variety
        exclude = ['owner']


class VarietySerializer(serializers.ModelSerializer):
    # crop =  serializers.StringRelatedField(many=False, read_only=True)
    crop_id = serializers.PrimaryKeyRelatedField(queryset = Crop.objects.all(), source='crop')

    class Meta:
        model = Variety
        # exclude = ['owner']
        fields = '__all__'
        depth = 1

class CropSerializer(serializers.ModelSerializer):
    varieties = VarietyShallowSerializer(many=True, read_only=True)
    # owner_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='owner')
    # owner = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Crop
        exclude = ['owner']
        # fields = '__all__'
        depth = 1

class PlantingSerializer(serializers.ModelSerializer):
    variety = VarietySerializer(many=False, read_only=True)
    variety_id = serializers.PrimaryKeyRelatedField(queryset = Variety.objects.all(), source='variety')

    class Meta:
        model = Planting
        fields = '__all__' 