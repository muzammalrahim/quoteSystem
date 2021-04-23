from rest_framework import serializers
from . import models


class ModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mode
        fields = '__all__'


class CommoditySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Commodity
        fields = '__all__'


class CarrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Carrier
        fields = '__all__'
