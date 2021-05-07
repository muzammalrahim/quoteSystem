from django.contrib import admin
from . import models
from django_admin_relation_links import AdminChangeLinksMixin
# class CountryAdmin(admin.ModelAdmin):
#     pass
#
class PortAdmin(AdminChangeLinksMixin, admin.ModelAdmin):
    list_display = ['name']
    changelist_links = ['cbt_origin_port']

admin.site.register(models.Country)
admin.site.register(models.Port, PortAdmin)

