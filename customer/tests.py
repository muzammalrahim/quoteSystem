from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Customer

class CountryTests(APITestCase):
    def test_create_customer(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('customer-list')
        data = {'name':'Kamran', 'email':'kamran@gmail.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Customer.objects.get().name, 'Pakistan')
        self.assertEqual(Customer.objects.get().code, 'PK')
