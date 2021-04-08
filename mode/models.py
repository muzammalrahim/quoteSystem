from django.db import models
from django.utils.translation import ugettext_lazy as _

class Mode(models.Model):
    name = models.CharField(_('mode'),max_length=30, null=False, blank=False)
    description = models.TextField(max_length=200, blank=True, null=True)
    created_at = models.DateField(blank=True, null=True,auto_now_add=True)
    updated_at = models.DateField(blank=True, null=True,auto_now=True)

    class Meta:
        db_table = 'qms_mode'


    def __str__(self):
        return str(self.name)


class Comodity(models.Model):
    name = models.CharField(_('name'),max_length=30, null=False, blank=False)
    created_at = models.DateField(blank=True, null=True,auto_now_add=True)
    updated_at = models.DateField(blank=True, null=True,auto_now=True)

    class Meta:
        db_table = 'qms_comodity'
        verbose_name = 'Comoditie'

    def __str__(self):
        return str(self.name)
