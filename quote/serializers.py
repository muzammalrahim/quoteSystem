from rest_framework import serializers
from country.serializers import PortSerializer
from mode.serializers import CommoditySerializer, ModeSerializer, CarrierSerializer, ChargeCodeSerializer
from . import models


class QuoteSerializer(serializers.ModelSerializer):
    # commodity = CommoditySerializer(read_only=True)
    # origin = PortSerializer(read_only=True)
    # destination = PortSerializer(read_only=True)
    # mode = ModeSerializer(read_only=True)
    # carrier = CarrierSerializer(read_only=True)

    class Meta:
        model = models.Quote
        fields = '__all__'


class CompanyBaseTariffSerializer(serializers.ModelSerializer):
    # charge_code = ChargeCodeSerializer(read_only=True)
    def to_representation(self, instance):
        representation = super(CompanyBaseTariffSerializer, self).to_representation(instance)
        representation['charge_code'] = ChargeCodeSerializer(instance.charge_code).data
        return representation

    class Meta:
        model = models.CompanyBaseTariff
        fields = '__all__'
