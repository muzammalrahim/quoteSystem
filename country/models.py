from django.db import models
from django.utils.translation import ugettext_lazy as _
from mode.models import ChargeCode


class Country(models.Model):
    name = models.CharField(_('country name'), max_length=30, null=False, blank=False)
    code = models.CharField(_('country code'), max_length=5, null=False, blank=False)
    created_at = models.DateField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateField(blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 'qms_country'
        verbose_name = 'countrie'

    def __str__(self):
        return str(self.name)


class Port(models.Model):
    name = models.CharField(_('name'), max_length=30, null=True, blank=True)
    description = models.TextField(max_length=200, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    charge_code = models.ManyToManyField(ChargeCode)
    created_at = models.DateField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateField(blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 'qms_port'

    def __str__(self):
        return str(self.name)
