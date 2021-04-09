from django.contrib import admin
from django.contrib.auth.models import *
from django.contrib.sites.models import Site
from . import models


class UserAdmin(admin.ModelAdmin):
	pass


admin.site.register(models.User, UserAdmin)

admin.site.unregister(Group)
admin.site.unregister(Site)
