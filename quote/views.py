from .models import Quote
from rest_framework import viewsets
from .serializers import QuoteSerializer
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
class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
