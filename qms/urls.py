from allauth.account.views import confirm_email
from django.contrib import admin
from django.urls import path, include

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
	openapi.Info(
		title="CMS API",
		default_version='v1',
		description="CMS Backend api",
		terms_of_service="https://www.google.com/policies/terms/",
		contact=openapi.Contact(email="creative.joomdev@gmail.com"),
		license=openapi.License(name="BSD License"),
	),
	public=True,
	permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
	path('admin/', admin.site.urls),
	url(r'^swagger(?P<format>\.json|\.yaml)$',
		schema_view.without_ui(cache_timeout=0), name='schema-json'),
	url(r'^$', schema_view.with_ui('swagger', cache_timeout=0),
		name='schema-swagger-ui'),
	url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
		name='schema-redoc'),
	# path(r'auth/', include('rest_auth.urls')),
	# path(r'register/', include('allauth.urls')),
	# path(r'^account/', include('allauth.urls')),
	path('api/', include('api.urls')),
	# path(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email,
	# 	 name='account_confirm_email'),
]
