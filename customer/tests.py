from rest_framework import status
from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from .serializers import CustomerSerializer
from .models import Customer

class CustomerTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('api.urls')),
    ]
    def setUp(self):
        Customer.objects.create(
            email='atta@gmail.com',name='Atta', phone='36584796854')
        Customer.objects.create(
            email='attagahk@gmail.com',name='Gahk', phone='94587968546')
        Customer.objects.create(
            email='kamran@gmail.com',name='Kamran', phone='11545879658')

    def test_create_customer(self):
        url = reverse('customer-list')

        # CREATE COUNTRY
        customer =  {'email':'sharoon@gmail.com','name':'Sharoon', 'phone':'66666666666'}
        response = self.client.post(url, customer, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        customer = Customer.objects.filter(email='sharoon@gmail.com').first()
        serializer = CustomerSerializer(customer)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(Customer.objects.count(), 4)

    def test_get_all_customers(self):
        response = self.client.get(reverse('customer-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # get data from db
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(customers.count(),3)

    def test_get_customer_by_id(self):
        customer = Customer.objects.filter(email='atta@gmail.com').first()
        url = '/api/customer/' + str(customer.id) + '/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = CustomerSerializer(customer)
        self.assertEqual(serializer.data,response.data)

    def test_update_customer(self):
        customer = Customer.objects.filter(name='Gahk').first()
        data = {"email":"attagahk@gmail.com",'name':'Kamran Atta', 'phone':'88888888888'}
        url = '/api/customer/' + str(customer.id) + '/'
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Kamran Atta')
        self.assertEqual(response.data['email'], 'attagahk@gmail.com')
        self.assertEqual(response.data['phone'], '88888888888')

    def test_patch_customer(self):
        customer = Customer.objects.create(email='kamal@gmail.com',name='Kamran', phone='22222222222')
        data = {'name':'Kamal Hussain'}
        url = '/api/customer/' + str(customer.id) + '/'
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Kamal Hussain')
        self.assertEqual(response.data['email'], 'kamal@gmail.com')
        self.assertEqual(response.data['phone'], '22222222222')
        self.assertEqual(Customer.objects.all().count(), 4)

    def test_delete_customer(self):
        customer = Customer.objects.filter(email='atta@gmail.com').first()
        url = '/api/customer/' + str(customer.id) + '/'
        total_before_delete = Customer.objects.all().count()
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        total_after_delete = Customer.objects.all().count()
        print(total_before_delete,total_after_delete)
        self.assertEqual(total_before_delete, total_after_delete + 1)


