from rest_framework.test import APITestCase
from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APIClient
import json
from mode.models import Mode
from user.models import User


class ModeTests(APITestCase):
    def setUp(self):
        user = User.objects.create(email='kami@gmail.com',password="demo")
        self.client.force_authenticate(user=user)

    def test_create_mode(self):
        url = reverse('mode-list')
        data = {'name': 'Australia'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Mode.objects.count(), 1)
        self.assertEqual(Mode.objects.get().name, 'Australia')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        print('Test create Mode Passed!')

    def test_get_all_mode(self):
        url = reverse('mode-list')
        data = {'name': 'Australia'}
        response = self.client.post(url, data, format='json')
        list_id = json.loads(response.content)['id']
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Mode.objects.count(), 1)
        self.assertEqual(list_id, 3)
        print('Test get all Modes Passed!')

    def test_delete_mode(self):
        mode = Mode.objects.create(name='Australia')
        url = '/api/mode/' + str(mode.id) + '/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        print('Test delete Mode Passed!')

    def test_patch_mode(self):
        mode = Mode.objects.create(name='Pakistan')
        data = {'name': 'jjjjj'}
        url = '/api/mode/' + str(mode.id) + '/'
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'jjjjj')
        self.assertEqual(Mode.objects.all().count(), 1)
        print('Test patch Mode Passed!')
