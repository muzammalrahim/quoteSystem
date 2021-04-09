from . import models
from . import serializers
from rest_framework import viewsets


class ModeViewSet(viewsets.ModelViewSet):
	queryset = models.Mode.objects.all()
	serializer_class = serializers.ModeSerializer


class ComodityViewSet(viewsets.ModelViewSet):
	queryset = models.Comodity.objects.all()
	serializer_class = serializers.ComoditySerializer
