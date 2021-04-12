from rest_framework import serializers
from . import models


class CountrySerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Country
		fields = '__all__'


class PortSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Port
		fields = '__all__'
		depth = 1
