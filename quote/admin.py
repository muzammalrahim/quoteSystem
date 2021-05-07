from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from django_admin_relation_links import AdminChangeLinksMixin
from mode.models import Carrier
from . import models


class CountryBaseTariffAdmin(AdminChangeLinksMixin,admin.ModelAdmin):
    # save_on_top = True
    list_display = (
        'origin_name', 'destination_link', 'mode', 'currency', 'get_name', 'srv_lel', 'comment', 'frequency',
        'unit_type',
        'start_date',
        'frequency_unit',

    )
    # list_display_links = ('origin_name','destination_name','unit_type', 'frequency_unit')
    change_links = ['destination']
    list_filter = ('start_date',)
    # change_list_template = 'templates/admin/change_list.html'


    def get_name(self, obj):
        return obj.carrier.code

    get_name.short_description = 'carrier'

    def mode_name(self, obj):
        return obj.mode.name

    mode_name.name = 'Mode'

    def origin_name(self, obj):
        return obj.origin.name

    origin_name.name = "origin"

    def destination_name(self, obj):
        return obj.destination.name

    destination_name.name = "destination"

    # def has_add_permission(self, request):
    #     return False


class QouteAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'weight_type', 'weight', 'goods_value', 'volume_type', 'volume', 'commodity', 'mode',
        'carrier','origin','destination'

    )

admin.site.register(models.Quote,QouteAdmin)
admin.site.register(models.CompanyBaseTariff, CountryBaseTariffAdmin)
