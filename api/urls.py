from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from country import views as country_views
from mode import views as mode_views
from customer import views as customer_views
from user import views as user_views
from quote import views as quote_view

router = DefaultRouter()

router.register(r'user', user_views.UserViewSet)

router.register(r'quote_view', quote_view.QuoteViewSet)
router.register(r'company_base_tariff', quote_view.CompanyBaseTariffViewSet)
router.register(r'country', country_views.CountryViewSet)
router.register(r'port', country_views.PortViewSet)

router.register(r'mode', mode_views.ModeViewSet)
router.register(r'commodity', mode_views.CommodityViewSet)
router.register(r'carrier', mode_views.CarrierViewSet)
router.register(r'calculator', mode_views.CalculatorViewSet)
router.register(r'chargecode', mode_views.ChargeCodeViewSet)
router.register(r'customer', customer_views.CustomerViewSet)

urlpatterns = format_suffix_patterns([
    path('accounts/', include('rest_registration.api.urls'))

])

urlpatterns += [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
