from django.shortcuts import render
from . import models
from . import serializers
from rest_framework import viewsets
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_201_CREATED
)

class ModeViewSet(viewsets.ModelViewSet):
    queryset = models.Mode.objects.all()
    serializer_class = serializers.ModeSerializer

class ComodityViewSet(viewsets.ModelViewSet):
    queryset = models.Comodity.objects.all()
    serializer_class = serializers.ComoditySerializer
