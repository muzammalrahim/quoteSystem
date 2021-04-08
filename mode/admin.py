from django.contrib import admin
from . import models

class ModeAdmin(admin.ModelAdmin):
    pass

class ComodityAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Mode, ModeAdmin)
admin.site.register(models.Comodity, ComodityAdmin)

