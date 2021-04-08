from rest_framework import serializers
from . import models

class CountrySerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    code = serializers.CharField(required=True)

    class Meta:
        model = models.Country
        fields = '__all__'


class PortSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)

    class Meta:
        model = models.Port
        fields = '__all__'
        depth=1