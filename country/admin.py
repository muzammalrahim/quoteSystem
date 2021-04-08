from django.contrib import admin
from . import models

class CountryAdmin(admin.ModelAdmin):
    pass

class PortAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Country, CountryAdmin)
admin.site.register(models.Port, PortAdmin)

