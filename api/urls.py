from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from country import views as country_views
from mode import views as mode_views
from customer import views as customer_views
from user import views as user_views

router = DefaultRouter()

router.register(r'user', user_views.UserViewSet)

router.register(r'country', country_views.CountryViewSet)
router.register(r'port', country_views.PortViewSet)


router.register(r'mode', mode_views.ModeViewSet)
router.register(r'comodity', mode_views.ComodityViewSet)

router.register(r'customer',customer_views.CustomerViewSet)

urlpatterns = [
    path('', include(router.urls))
    # path('user/', user_views.UserViewSet),
    # path('api-auth/', include('rest_framework.urls'))
]