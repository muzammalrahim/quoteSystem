from rest_framework.test import APITestCase, URLPatternsTestCase
from django.urls import include, path, reverse
from rest_framework import status
import json
from mode.models import Mode, Comodity
from mode.serializers import ComoditySerializer, ModeSerializer
from user.models import User


class ModeTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('api.urls')),
    ]

    def setUp(self):
        user = User.objects.create(email='kami@gmail.com', password="demo")
        self.client.force_authenticate(user=user)
        Mode.objects.create(
            name='Australia')

    def test_create_mode(self):
        url = reverse('mode-list')
        data = {'name': 'pak'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Mode.objects.count(), 2)
        # self.assertEqual(Mode.objects.get().name, 'pak')
        # response = self.client.get(url, format='json')
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(len(response.data), 2)
        print('Test create Mode Passed!')

    def test_get_all_mode(self):
        response = self.client.get(reverse('mode-list'))
        mode = Mode.objects.all()
        serializer = ModeSerializer(mode, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(mode.count(), 1)
        print("Test get all mode passed")

    def test_get_mode_by_id(self):
        mode = Mode.objects.filter(name='Australia').first()
        url = '/api/mode/' + str(mode.id) + '/'
        response = self.client.get(url)
        serializer = ModeSerializer(mode)
        self.assertEqual(serializer.data, response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("Test get mode by id passed")

    def test_update_mode(self):
        mode = Mode.objects.filter(name='Australia').first()
        data = {"name": "eengsss"}
        url = '/api/mode/' + str(mode.id) + '/'
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'eengsss')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("Test Update mode")

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
        comodity = Comodity.objects.all()
        serializer = ComoditySerializer(comodity, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'jjjjj')
        self.assertEqual(Mode.objects.all().count(), 2)
        print('Test patch Mode Passed!')
        self.assertEqual(Mode.objects.all().count(), 2)
        print('Test  patch mode Passed!')


class ComodityTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('api.urls')),
    ]

    def setUp(self):
        user = User.objects.create(email='kami@gmail.com', password="demo")
        self.client.force_authenticate(user=user)

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
        print("Test Create Comodity Passed")

    def test_get_all_comodity(self):
        response = self.client.get(reverse('comodity-list'))
        comodity = Comodity.objects.all()
        serializer = ComoditySerializer(comodity, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(comodity.count(), 4)
        print("Test get all comodity passed")

    def test_get_comodity_by_id(self):
        comodity = Comodity.objects.filter(name='India').first()
        url = '/api/comodity/' + str(comodity.id) + '/'
        response = self.client.get(url)
        serializer = ComoditySerializer(comodity)
        self.assertEqual(serializer.data, response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("Test get comodity by id passed")

    def test_update_comodity(self):
        comodity = Comodity.objects.filter(name='India').first()
        data = {"name": "eengsss"}
        url = '/api/comodity/' + str(comodity.id) + '/'
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'eengsss')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("Test Update Comodity")

    def test_patch_comodity(self):
        comodity = Comodity.objects.create(name="england")
        data = {'name': 'englanssss'}
        url = '/api/comodity/' + str(comodity.id) + '/'
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'englanssss')
        self.assertEqual(Comodity.objects.all().count(), 5)
        print("Test Patch Comodity Passed")

    def test_delete_comodity(self):
        comodity = Comodity.objects.create(name="england")
        url = '/api/comodity/' + str(comodity.id) + '/'
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        print("Test delete comodity passed")
