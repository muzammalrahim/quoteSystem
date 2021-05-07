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
		title="QMS API",
		default_version='v1',
		description="QMS Backend api",
		terms_of_service="https://www.google.com/policies/terms/",
		contact=openapi.Contact(email="creative.joomdev@gmail.com"),
		license=openapi.License(name="BSD License"),
	),
	public=True,
	permission_classes=(permissions.AllowAny,),
)
admin.site.site_header = 'QMS'
admin.site.site_title = 'Welcome to the QMS Portal'
admin.site.index_title = 'Welocme to the QMS Dashboard'
urlpatterns = [
	path('admin/', admin.site.urls),
	url(r'^swagger(?P<format>\.json|\.yaml)$',
		schema_view.without_ui(cache_timeout=0), name='schema-json'),
	url(r'^$', schema_view.with_ui('swagger', cache_timeout=0),
		name='schema-swagger-ui'),
	url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
		name='schema-redoc'),
	# path('api/quote_view', quote_view),
	path('api/', include('api.urls')),
]
