from django.test import TestCase
from rest_framework.test import APITestCase
from user.models import User
from django.urls import reverse
from rest_framework import status


# Create your tests here.
class RegisterUserTest(APITestCase):
    def setUp(self):
        self.test_user = User.objects.create_user('testuser@gmail.com', 'testpassword')
        self.client.force_authenticate(user=self.test_user)
        print('Test User is authenticated!!')
        # self.create_url = '/api/accounts/register/' + str(self.test_user.id) + '/'
        self.create_url = reverse('user-list')

    def test_create_user(self):
        data = {
            "first_name": "hello",
            "last_name": "1hello",
            "username": "foxxobar",
            "email": "foxxobar@example.com",
            "password": "somexpassword",
            "activated": True
        }
        response = self.client.post(self.create_url, data, format='json')

        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['email'], data['email'])
        print('Test create user successful!')

    def test_user_login(self):
        response = self.client.login(email='testuser@gmail.com', password='testpassword')
        self.assertEqual(response, True)
        self.assertEqual(User.objects.count(), 1)
        print('Test login user successful!')

    def test_user_logout(self):
        response = self.client.logout()
        self.assertEqual(response, None)
        print('Test logout user successful!')
