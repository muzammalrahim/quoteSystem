from rest_framework import serializers
from country.serializers import PortSerializer
from mode.serializers import ComoditySerializer
from .models import Quote


class QuoteSerializer(serializers.ModelSerializer):
    comodity = ComoditySerializer(read_only=True)
    port = PortSerializer(read_only=True)

    class Meta:
        model = Quote
        fields = '__all__'
        # depth = 1
