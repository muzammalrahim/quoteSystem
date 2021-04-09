from django.test import TestCase
import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .serializers import CountrySerializer
from .models import Country, Port

class CountryTests(APITestCase):
    def setUp(self):
        Country.objects.create(
            name='Australia', code='AUS')
        Country.objects.create(
            name='India', code='IND')
        Country.objects.create(
            name='Pakistan', code='PK')
        Country.objects.create(
            name='Sri lanka', code='SRI')

    def test_create_country(self):
        url = reverse('country-list')

        # CREATE COUNTRY
        country = {'name': 'India', 'code': 'IND'}
        response = self.client.post(url, country, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Country.objects.count(), 5)

        # CREATE PORT
        # url = reverse('port-list')
        # port = {
        #     'name':	'Gawadar',
        #     'country': 1
        #     # 'country':{
        #     #     'id':1,
        #     #     'name':'Pakistan',
        #     #     'code': 'PK'
        #     # }
        #
        #     }
        # response = self.client.post(url, port, format='json')
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(Port.objects.count(), 1)
        # self.assertEqual(Port.objects.get().name, 'India')
        # self.assertEqual(Port.objects.get().country.code, 'IND')

    def test_get_all_countries(self):
        response = self.client.get(reverse('country-list'))
        # get data from db
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(countries.count(),4)

    # def test_get_country_by_name(self):
    #     # get API response
    #     response = self.client.get(reverse('/country-list/3/'))
    #     # get data from db
    #     country = Country.objects.get(name='Pakistan')
    #     serializer = CountrySerializer(country)
    #     # self.assertEqual(response, serializer.data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(country.count(), 10)


