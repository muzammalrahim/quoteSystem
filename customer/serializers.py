from rest_framework import serializers
from . import models

class CustomerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)

    class Meta:
        model = models.Customer
        fields = '__all__'