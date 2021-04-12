from django.test import TestCase
from rest_framework.test import APITestCase
from user.models import User
from django.urls import reverse

# Create your tests here.
class RegisterUserTest(APITestCase):
    def setUp(self):
        self.test_user = User.objects.create_user('testuser@gmail.com', 'testpassword')
        self.create_url = reverse('account-create')
    def test_create_user(self):
        data = {
            "email" : "foxxobar@gmail.com"
        }
        response = self.client.post(self.create_url, format='json')
        self.assertEqual(User.objects.count(),2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], data['email'])
