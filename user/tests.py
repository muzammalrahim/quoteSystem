from rest_framework import permissions
from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from .serializers import UserSerializer
from .models import User

class CustomerTests(APITestCase, URLPatternsTestCase):
    permissions_classes = [permissions.AllowAny,]
    urlpatterns = [
        path('api/', include('api.urls')),
    ]
    def setUp(self):
        User.objects.create(
            email='kamranatta@gmail.com')
        User.objects.create(
            email='kamran@gmail.com')
        user = {'email':'kamrangahk@gmail.com', "password":''}
        user = self.client.post()


