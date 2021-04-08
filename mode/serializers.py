from rest_framework import serializers
from . import models

class ModeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)

    class Meta:
        model = models.Mode
        fields = '__all__'


class ComoditySerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)

    class Meta:
        model = models.Comodity
        fields = '__all__'