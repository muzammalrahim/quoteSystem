from django.shortcuts import render
from . import models
from . import serializers
from rest_framework import viewsets
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_201_CREATED
)

class CountryViewSet(viewsets.ModelViewSet):
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer

class PortViewSet(viewsets.ModelViewSet):
    queryset = models.Port.objects.all()
    serializer_class = serializers.PortSerializer
