from rest_framework.test import APITestCase, URLPatternsTestCase
from django.urls import include, path, reverse
from rest_framework import status
from country.models import Port
from mode.models import Comodity
from quote.models import Quote
from quote.serializers import QuoteSerializer
from user.models import User


class QuoteTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('api.urls')),
    ]

    def setUp(self):
        user = User.objects.create(email='kami@gmail.com', password="demo")
        self.client.force_authenticate(user=user)
        comodity = Comodity.objects.create(
            name='comodity')
        port = Port.objects.create(
            name='Gawadar')
        Quote.objects.create(name='first', comodity=comodity, port=port)

    def test_create_quote(self):
        url = reverse('quote-list')
        quote = {'name': 'quottt', 'comodity': (Comodity.objects.filter(name='comodity').first()).id
            , 'port': (Port.objects.filter(name='Gawadar').first()).id}
        total_before_create = Quote.objects.count()
        response = self.client.post(url, quote, format='json')
        total_after_create = Quote.objects.count()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(total_before_create, total_after_create - 1)
        print('Test create Quote successful!')

    def test_get_all_quote(self):
        response = self.client.get(reverse('quote-list'))
        # get data from db
        quote = Quote.objects.all()
        serializer = QuoteSerializer(quote, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(quote.count(), 1)
        print('Test retrieve all Quote successful!')

    def test_get_quote_by_id(self):
        quote = Quote.objects.filter(name='first').first()
        url = '/api/quote_view/' + str(quote.id) + '/'
        response = self.client.get(url)
        serializer = QuoteSerializer(quote)
        # self.assertEqual(serializer.data['name'], response.data['name'])
        self.assertEqual(serializer.data, response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print('Test retrieve Quote successful!')

    def test_update_quote(self):
        quote = Quote.objects.filter(name='first').first()
        comodity = Comodity.objects.filter(name='comodity').first()
        port = Port.objects.filter(name='Gawadar').first()
        data = {"name": "comodity update", 'comodity': comodity.id, 'port': port.id}
        url = '/api/quote_view/' + str(quote.id) + '/'
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'comodity update')
        self.assertEqual(response.data['name'], 'comodity update')
        # self.assertEqual(response.data['comodity'], comodity.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print('Test update Quote successful!')

    def test_patch_quote(self):
        comodity = Comodity.objects.filter(name='comodity').first()
        quote = Quote.objects.create(name='first', comodity=comodity)
        data = {'name': 'Port Qasim'}
        url = '/api/quote_view/' + str(quote.id) + '/'
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Port Qasim')
        self.assertEqual(Quote.objects.count(), 2)
        print('Test patch Port successful!')

    def test_delete_quote(self):
        quote = Quote.objects.filter(name='first').first()
        url = '/api/quote_view/' + str(quote.id) + '/'
        total_before_delete = Quote.objects.count()
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        total_after_delete = Quote.objects.count()
        self.assertEqual(total_before_delete, total_after_delete + 1)
        print('Test delete Quote successful!')
