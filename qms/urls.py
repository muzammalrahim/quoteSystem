from allauth.account.views import confirm_email
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'auth/', include('rest_auth.urls')),
    # path(r'register/', include('allauth.urls')),
    # path(r'^account/', include('allauth.urls')),
    path('api/', include('api.urls')),
    path(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),
]
