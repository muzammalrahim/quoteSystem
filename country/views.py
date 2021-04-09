from . import models
from . import serializers
from rest_framework import viewsets


class CountryViewSet(viewsets.ModelViewSet):
	queryset = models.Country.objects.all()
	serializer_class = serializers.CountrySerializer


class PortViewSet(viewsets.ModelViewSet):
	queryset = models.Port.objects.all()
	serializer_class = serializers.PortSerializer
