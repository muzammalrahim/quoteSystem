from django.contrib import admin
from . import models

# class ModeAdmin(admin.ModelAdmin):
#     pass
#
# class ComodityAdmin(admin.ModelAdmin):
#     pass

admin.site.register(models.Mode)
admin.site.register(models.Commodity)
admin.site.register(models.Carrier)
