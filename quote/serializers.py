from rest_framework import serializers
from country.serializers import PortSerializer
from mode.serializers import CommoditySerializer, ModeSerializer, CarrierSerializer
from .models import Quote


class QuoteSerializer(serializers.ModelSerializer):
    # commodity = CommoditySerializer(read_only=True)
    # origin = PortSerializer(read_only=True)
    # destination = PortSerializer(read_only=True)
    # mode = ModeSerializer(read_only=True)
    # carrier = CarrierSerializer(read_only=True)

    class Meta:
        model = Quote
        fields = '__all__'
        # depth = 1
