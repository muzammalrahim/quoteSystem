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
