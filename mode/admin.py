from django.contrib import admin
from . import models


# class ModeAdmin(admin.ModelAdmin):
#     pass
#
# class ComodityAdmin(admin.ModelAdmin):
#     pass

class CalculatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class ChargeCodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'local_description', 'company_base_tariff', 'calculator')


admin.site.register(models.Mode)
admin.site.register(models.Commodity)
admin.site.register(models.Carrier)
admin.site.register(models.Calculator, CalculatorAdmin)
admin.site.register(models.ChargeCode, ChargeCodeAdmin)
