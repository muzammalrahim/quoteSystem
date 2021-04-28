from django.db import models
from django.utils.translation import ugettext_lazy as _

from quote.models import CompanyBaseTariff


class Mode(models.Model):
    name = models.CharField(_('name'), max_length=30, null=False, blank=False)
    description = models.TextField(max_length=200, blank=True, null=True)
    created_at = models.DateField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateField(blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 'qms_mode'
    #
    # def __str__(self):
    #     return str(self.name)


class Commodity(models.Model):
    code = models.CharField(_('code'), max_length=30, null=False, blank=False)
    description = models.TextField(max_length=200, blank=True, null=True)
    created_at = models.DateField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateField(blank=True, null=True, auto_now=True)

    class Meta:
        db_table = 'qms_comodity'
        verbose_name = 'Comoditie'
    #
    # def __str__(self):
    #     return str(self.name)


class Carrier(models.Model):
    code = models.CharField(_('code'), max_length=30, null=False, blank=False)
    description = models.TextField(max_length=200, blank=True, null=True)


class Calculator(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    description = models.TextField(max_length=200, blank=True, null=True)


class ChargeCode(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    description = models.TextField(max_length=200, blank=True, null=True)
    local_description = models.TextField(max_length=200, blank=True, null=True)
    company_base_tariff = models.ForeignKey(CompanyBaseTariff, on_delete=models.SET_NULL, blank=True, null=True)
    calculator = models.ForeignKey(Calculator, on_delete=models.SET_NULL, blank=True, null=True)





