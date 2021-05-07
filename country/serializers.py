from rest_framework import serializers

from mode.serializers import ChargeCodeSerializer
from . import models


class CountrySerializer(serializers.ModelSerializer):
	# id = serializers.IntegerField()
	class Meta:
		model = models.Country
		fields = '__all__'


class PortSerializer(serializers.ModelSerializer):
	def to_representation(self, instance):
		representation = super(PortSerializer, self).to_representation(instance)
		representation['charge_code'] = ChargeCodeSerializer(instance.charge_code, many=True).data
		return representation
	class Meta:
		model = models.Port
		fields = '__all__'
		# depth = 1
