from rest_framework import status
from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from .serializers import CountrySerializer, PortSerializer
from .models import Country, Port
from user.models import User

class CountryTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('api.urls')),
    ]
    def setUp(self):
        user = User.objects.create(email='kami@gmail.com',password="demo")
        self.client.force_authenticate(user=user)
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
        print('Test create Country Passed!')

    def test_get_all_countries(self):
        response = self.client.get(reverse('country-list'))
        # get data from db
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(countries.count(),4)
        print('Test get all Countries Passed!')

    def test_get_country_by_id(self):
        country = Country.objects.filter(code='AUS').first()
        url = '/api/country/' + str(country.id) + '/'
        response = self.client.get(url)
        serializer = CountrySerializer(country)
        self.assertEqual(serializer.data,response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print('Test get Country by id Passed!')

    def test_update_country(self):
        country = Country.objects.filter(name='Pakistan').first()
        data = {"name":"England",'code':'ENG'}
        url = '/api/country/' + str(country.id) + '/'
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'England')
        self.assertEqual(response.data['code'], 'ENG')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print('Test update Country Passed!')

    def test_patch_country(self):
        country = Country.objects.create(name='Pakistan', code='IND')
        data = {'code':'PK'}
        url = '/api/country/' + str(country.id) + '/'
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['code'], 'PK')
        self.assertEqual(Country.objects.all().count(), 5)
        print('Test patch Country Passed!')

    def test_delete_country(self):
        country = Country.objects.filter(code='SRI').first()
        url = '/api/country/' + str(country.id) + '/'
        total_before_delete = Country.objects.all().count()
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        total_after_delete = Country.objects.all().count()
        print(total_before_delete,total_after_delete)
        self.assertEqual(total_before_delete, total_after_delete + 1)
        print('Test delete Country Passed!')


# TEST CASES FOR  OF PORT MODULE

class PortTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('api.urls')),
    ]
    def setUp(self):
        user = User.objects.create(email='kami@gmail.com',password="demo")
        self.client.force_authenticate(user=user)
        india=Country.objects.create(
            name='India', code='IND')
        pakistan=Country.objects.create(
            name='Pakistan', code='PK')

        Port.objects.create(
            name='Gawadar Port', country=pakistan)
        Port.objects.create(
            name='Mumbai Port', country=india)

    def test_create_port(self):
        url = reverse('port-list')

        # CREATE COUNTRY
        port = {'name': 'Balochistan', 'country': (Country.objects.filter(name='Pakistan').first()).id}
        total_before_create = Port.objects.count()
        response = self.client.post('/api/port/', port, format='json')
        total_after_create = Port.objects.count()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(total_before_create, total_after_create -1)
        print('Test create Port successful!')

    def test_get_all_ports(self):
        response = self.client.get(reverse('port-list'))
        # get data from db
        ports = Port.objects.all()
        serializer = PortSerializer(ports, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ports.count(),2)
        print('Test retrieve all Ports successful!')

    def test_get_port_by_id(self):
        port = Port.objects.filter(name='Gawadar Port').first()
        url = '/api/port/' + str(port.id) + '/'
        response = self.client.get(url)
        serializer = PortSerializer(port)
        self.assertEqual(serializer.data['name'], response.data['name'])
        self.assertEqual(serializer.data,response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print('Test retrieve Port successful!')

    def test_update_port(self):
        port = Port.objects.filter(name='Mumbai Port').first()
        country = Country.objects.filter(name='India').first()
        data = {"name":"Delhi Port", 'country':country.id}
        url = '/api/port/' + str(port.id) + '/'
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Delhi Port')
        self.assertEqual(response.data['country'], country.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print('Test update Port successful!')

    def test_patch_port(self):
        country = Country.objects.filter(name='Pakistan').first()
        port = Port.objects.create(name='Sindh Port', country=country)
        data = {'name':'Port Qasim'}
        url = '/api/port/' + str(port.id) + '/'
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Port Qasim')
        self.assertEqual(Port.objects.count(), 3)
        print('Test patch Port successful!')

    def test_delete_port(self):
        port = Port.objects.filter(name='Mumbai Port').first()
        url = '/api/port/' + str(port.id) + '/'
        total_before_delete = Port.objects.count()
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        total_after_delete = Port.objects.count()
        self.assertEqual(total_before_delete, total_after_delete + 1)
        print('Test delete Port successful!')