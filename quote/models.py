from django.db import models
from country.models import Port
from mode.models import Comodity


class Quote(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    comodity = models.ForeignKey(Comodity, on_delete=models.SET_NULL, blank=True,
                                 null=True)
    port = models.ForeignKey(Port, on_delete=models.SET_NULL, blank=True,
                                 null=True)
