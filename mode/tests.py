from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
import json
from mode.models import Mode, Comodity


class ModeTests(APITestCase):
    # def setUp(self):
    #     self.password = 'test'
    #     self.email = 'admin@mgmail.com'
    #
    #     self.user = User.objects.create(self.email, self.password)
    #
    #     self.client = APIClient()
    #     self.client.force_authenticate(email=self.email, password=self.password)
    # urlpatterns = [
    #     path('api/', include('api.urls')),
    # ]

    def test_create_mode(self):
        url = reverse('mode-list')
        data = {'name': 'Australia'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Mode.objects.count(), 1)
        self.assertEqual(Mode.objects.get().name, 'Australia')
        # response = self.client.get(url, format='json')
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(len(response.data), 1)

    def test_get_all_mode(self):
        url = reverse('mode-list')
        data = {'name': 'Australia'}
        response = self.client.post(url, data, format='json')
        list_id = json.loads(response.content)['id']
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Mode.objects.count(), 1)
        self.assertEqual(list_id, 3)

    def test_delete_mode(self):
        mode = Mode.objects.create(name='Australia')
        url = '/api/mode/' + str(mode.id) + '/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_patch_mode(self):
        mode = Mode.objects.create(name='Pakistan')
        data = {'name': 'jjjjj'}
        url = '/api/mode/' + str(mode.id) + '/'
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'jjjjj')
        self.assertEqual(Mode.objects.all().count(), 1)


class ComodityTests(APITestCase):
    def test_create_comodity(self):
        url = reverse('comodity-list')
        data = {'name': 'Australia'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comodity.objects.count(), 1)
        self.assertEqual(Comodity.objects.get().name, 'Australia')

    def test_get_all_comodity(self):
        url = reverse('comodity-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
