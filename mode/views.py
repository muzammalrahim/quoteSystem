from . import models
from . import serializers
from rest_framework import viewsets


class ModeViewSet(viewsets.ModelViewSet):
    queryset = models.Mode.objects.all()
    serializer_class = serializers.ModeSerializer


class CommodityViewSet(viewsets.ModelViewSet):
    queryset = models.Commodity.objects.all()
    serializer_class = serializers.CommoditySerializer


class CarrierViewSet(viewsets.ModelViewSet):
    queryset = models.Carrier.objects.all()
    serializer_class = serializers.CarrierSerializer


class CalculatorViewSet(viewsets.ModelViewSet):
    queryset = models.Calculator.objects.all()
    serializer_class = serializers.CalculatorSerializer


class ChargeCodeViewSet(viewsets.ModelViewSet):
    queryset = models.ChargeCode.objects.all()
    serializer_class = serializers.ChargeCodeSerializer

