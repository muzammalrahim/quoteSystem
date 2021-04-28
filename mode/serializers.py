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


class CalculatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Calculator
        fields = '__all__'


class ChargeCodeSerializer(serializers.ModelSerializer):
    # calculator = CalculatorSerializer(read_only=True)
    def to_representation(self, instance):
        representation = super(ChargeCodeSerializer, self).to_representation(instance)
        representation['calculator'] = CalculatorSerializer(instance.calculator).data
        return representation

    class Meta:
        model = models.ChargeCode
        fields = '__all__'
