from . import models
from rest_framework import viewsets
from . import serializers


class QuoteViewSet(viewsets.ModelViewSet):
    queryset = models.Quote.objects.all()
    serializer_class = serializers.QuoteSerializer


class CompanyBaseTariffViewSet(viewsets.ModelViewSet):
    queryset = models.CompanyBaseTariff.objects.all()
    serializer_class = serializers.CompanyBaseTariffSerializer

# from rest_framework.decorators import api_view
#
# from country import serializers
# from mode.models import Comodity, Mode
# from country.models import Port
# from rest_framework.response import Response
#
#
# @api_view(['GET'])
# def quote_view(requset):
#     comodity = Comodity.objects.values()
#     # serializers = serializers.Com
#     # mode = Mode.objects.all().values()
#     mode = Mode.objects.values()
#     # print("mode", mode)
#     port = Port.objects.values()
#     # serializer = serializers.PortSerializer(port, many=True)
#     # serializer.data
#
#     content = {
#         'comodity': comodity,
#         'mode': mode,
#         'port': port
#
#     }
#     return Response(content)
