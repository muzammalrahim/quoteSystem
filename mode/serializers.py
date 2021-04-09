from rest_framework import serializers
from . import models


class ModeSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Mode
		fields = '__all__'


class ComoditySerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Comodity
		fields = '__all__'
