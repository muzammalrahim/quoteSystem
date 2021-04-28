from rest_framework.test import APITestCase, URLPatternsTestCase
from django.urls import include, path, reverse
from rest_framework import status
import json
from mode.models import Mode, Commodity, Calculator, ChargeCode, Carrier
from mode.serializers import CommoditySerializer, ModeSerializer, ChargeCodeSerializer, CalculatorSerializer, \
    CarrierSerializer
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
        comodity = Commodity.objects.all()
        serializer = CommoditySerializer(comodity, many=True)
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

        Commodity.objects.create(
            name='Australia')
        Commodity.objects.create(
            name='India')
        Commodity.objects.create(
            name='Pakistan')
        Commodity.objects.create(
            name='Sri lanka')

    def test_create_comodity(self):
        url = reverse('comodity-list')
        data = {'name': 'Australia'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Commodity.objects.count(), 5)
        # self.assertEqual(Comodity.objects.get().name, 'Australia')
        print("Test Create Comodity Passed")

    def test_get_all_comodity(self):
        response = self.client.get(reverse('comodity-list'))
        comodity = Commodity.objects.all()
        serializer = CommoditySerializer(comodity, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(comodity.count(), 4)
        print("Test get all comodity passed")

    def test_get_comodity_by_id(self):
        comodity = Commodity.objects.filter(name='India').first()
        url = '/api/comodity/' + str(comodity.id) + '/'
        response = self.client.get(url)
        serializer = CommoditySerializer(comodity)
        self.assertEqual(serializer.data, response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("Test get comodity by id passed")

    def test_update_comodity(self):
        comodity = Commodity.objects.filter(name='India').first()
        data = {"name": "eengsss"}
        url = '/api/comodity/' + str(comodity.id) + '/'
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'eengsss')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("Test Update Comodity")

    def test_patch_comodity(self):
        comodity = Commodity.objects.create(name="england")
        data = {'name': 'englanssss'}
        url = '/api/comodity/' + str(comodity.id) + '/'
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'englanssss')
        self.assertEqual(Commodity.objects.all().count(), 5)
        print("Test Patch Comodity Passed")

    def test_delete_comodity(self):
        comodity = Commodity.objects.create(name="england")
        url = '/api/comodity/' + str(comodity.id) + '/'
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        print("Test delete comodity passed")


class CarrierTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('api.urls')),
    ]

    def setUp(self):
        user = User.objects.create(email='kami@gmail.com', password="demo")
        self.client.force_authenticate(user=user)

        Carrier.objects.create(
            description='Australia')
        Carrier.objects.create(
            description='India')
        Carrier.objects.create(
            description='Pakistan')
        Carrier.objects.create(
            description='Sri lanka')

    def test_create_carrier(self):
        url = reverse('carrier-list')
        data = {'description': 'Australia'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Carrier.objects.count(), 5)
        # self.assertEqual(Comodity.objects.get().name, 'Australia')
        print("Test Create Comodity Passed")

    def test_get_all_carrier(self):
        response = self.client.get(reverse('comodity-list'))
        carrier = Carrier.objects.all()
        serializer = CarrierSerializer(carrier, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(carrier.count(), 4)
        print("Test get all carrier passed")

    def test_get_carrier_by_id(self):
        carrier = Carrier.objects.filter(name='India').first()
        url = '/api/carrier/' + str(carrier.id) + '/'
        response = self.client.get(url)
        serializer = CarrierSerializer(carrier)
        self.assertEqual(serializer.data, response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("Test get comodity by id passed")

    def test_update_carrier(self):
        carrier = Carrier.objects.filter(name='India').first()
        data = {"name": "eengsss"}
        url = '/api/carrier/' + str(carrier.id) + '/'
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'eengsss')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("Test Update carrier")

    def test_patch_carrier(self):
        carrier = Carrier.objects.create(name="england")
        data = {'name': 'englanssss'}
        url = '/api/carrier/' + str(carrier.id) + '/'
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'englanssss')
        self.assertEqual(carrier.objects.all().count(), 5)
        print("Test Patch carrier Passed")

    def test_delete_carrier(self):
        carrier = Carrier.objects.create(name="england")
        url = '/api/carrier/' + str(carrier.id) + '/'
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        print("Test delete carrier passed")


class CalculatorTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('api.urls')),
    ]

    def setUp(self):
        user = User.objects.create(email='kami@gmail.com', password="demo")
        self.client.force_authenticate(user=user)

        Calculator.objects.create(
            name='Australia')
        Calculator.objects.create(
            name='India')
        Calculator.objects.create(
            name='Pakistan')
        Calculator.objects.create(
            name='Sri lanka')

    def test_create_calculator(self):
        url = reverse('calculator-list')
        data = {'name': 'Australia'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comodity.objects.count(), 5)
        # self.assertEqual(Comodity.objects.get().name, 'Australia')
        print("Test Create  Passed")

    def test_get_all_calculator(self):
        response = self.client.get(reverse('calculator-list'))
        calculator = Calculator.objects.all()
        serializer = CalculatorSerializer(calculator, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(calculator.count(), 4)
        print("Test get all Calculator passed")

    def test_get_calculator_by_id(self):
        calculator = Calculator.objects.filter(name='India').first()
        url = '/api/calculator/' + str(calculator.id) + '/'
        response = self.client.get(url)
        serializer = CalculatorSerializer(calculator)
        self.assertEqual(serializer.data, response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("Test get Calculator by id passed")

    def test_update_calculator(self):
        calculator = Calculator.objects.filter(name='India').first()
        data = {"name": "eengsss"}
        url = '/api/calculator/' + str(calculator.id) + '/'
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'eengsss')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("Test Update Calculator")

    def test_patch_calculator(self):
        calculator = Calculator.objects.create(name="england")
        data = {'name': 'englanssss'}
        url = '/api/calculator/' + str(calculator.id) + '/'
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'englanssss')
        self.assertEqual(Comodity.objects.all().count(), 5)
        print("Test Patch Calculator Passed")

    def test_delete_comodity(self):
        calculator = Calculator.objects.create(name="england")
        url = '/api/calculator/' + str(calculator.id) + '/'
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        print("Test delete calculator passed")


class ChargeCodeTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('api.urls')),
    ]

    def setUp(self):
        user = User.objects.create(email='kami@gmail.com', password="demo")
        self.client.force_authenticate(user=user)

        ChargeCode.objects.create(
            name='Australia')
        ChargeCode.objects.create(
            name='India')
        ChargeCode.objects.create(
            name='Pakistan')
        ChargeCode.objects.create(
            name='Sri lanka')

    def test_create_charge_code(self):
        url = reverse('charge_code-list')
        data = {'name': 'Australia'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ChargeCode.objects.count(), 5)
        # self.assertEqual(Comodity.objects.get().name, 'Australia')
        print("Test Create  Passed")

    def test_get_all_charge_code(self):
        response = self.client.get(reverse('charge_code-list'))
        charge_code = ChargeCode.objects.all()
        serializer = ChargeCodeSerializer(charge_code, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(charge_code.count(), 4)
        print("Test get all ChargeCode passed")

    def test_get_charge_code_by_id(self):
        charge_code = ChargeCode.objects.filter(name='India').first()
        url = '/api/charge_code/' + str(charge_code.id) + '/'
        response = self.client.get(url)
        serializer = ChargeCodeSerializer(charge_code)
        self.assertEqual(serializer.data, response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("Test get charge_code by id passed")

    def test_update_charge_code(self):
        charge_code = ChargeCode.objects.filter(name='India').first()
        data = {"name": "eengsss"}
        url = '/api/charge_code/' + str(charge_code.id) + '/'
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'eengsss')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("Test Update charge_code")

    def test_patch_charge_code(self):
        charge_code = ChargeCode.objects.create(name="england")
        data = {'name': 'englanssss'}
        url = '/api/charge_code/' + str(charge_code.id) + '/'
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'englanssss')
        self.assertEqual(ChargeCode.objects.all().count(), 5)
        print("Test Patch Calculator Passed")

    def test_delete_charge_code(self):
        charge_code = ChargeCode.objects.create(name="england")
        url = '/api/charge_code/' + str(charge_code.id) + '/'
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        print("Test delete calculator passed")
