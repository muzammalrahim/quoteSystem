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
    urlpatterns = [
        path('api/', include('api.urls')),
    ]

    def setUp(self):
        Mode.objects.create(
            name='Australia')

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
        self.assertEqual(Mode.objects.all().count(), 2)

    def test_delete_mode(self):
        mode = Mode.objects.create(name='Australia')
        url = '/api/mode/' + str(mode.id) + '/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class ComodityTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('api.urls')),
    ]

    def setUp(self):
        Comodity.objects.create(
            name='Australia')
        Comodity.objects.create(
            name='India')
        Comodity.objects.create(
            name='Pakistan')
        Comodity.objects.create(
            name='Sri lanka')

    def test_create_comodity(self):
        url = reverse('comodity-list')
        data = {'name': 'Australia'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comodity.objects.count(), 5)
        # self.assertEqual(Comodity.objects.get().name, 'Australia')

    def test_get_all_comodity(self):
        response = self.client.get(reverse('comodity-list'))
        comodity = Comodity.objects.all()
        serializer = ComoditySerializer(comodity, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(comodity.count(), 4)

    def test_get_comodity_by_id(self):
        comodity = Comodity.objects.filter(name='India').first()
        url = '/api/comodity/' + str(comodity.id) + '/'
        response = self.client.get(url)
        serializer = ComoditySerializer(comodity)
        self.assertEqual(serializer.data, response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_comodity(self):
        comodity = Comodity.objects.filter(name='India').first()
        data = {"name": "eengsss"}
        url = '/api/comodity/' + str(comodity.id) + '/'
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'eengsss')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_comodity(self):
        comodity = Comodity.objects.create(name="england")
        data = {'name': 'englanssss'}
        url = '/api/comodity/' + str(comodity.id) + '/'
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'englanssss')
        self.assertEqual(Comodity.objects.all().count(), 5)

    def test_delete_country(self):
        comodity = Comodity.objects.create(name="england")
        url = '/api/comodity/' + str(comodity.id) + '/'
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
