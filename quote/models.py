from django.db import models
from country.models import Port
from mode.models import Commodity, Carrier, Mode


class Quote(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    weight_choice = (
        ('KG', 'KG'),
        ('G', 'G'),
    )
    weigth_type = models.CharField(max_length=100, blank=True, null=True, choices=weight_choice)
    weight = models.FloatField(null=True, blank=True)
    goods_value = models.IntegerField(blank=True, null=True)
    volume_choice = (
        ('M3', 'M3'),
        ('M2', 'M2'),
        ('M1', 'M1'),
    )
    volume_type = models.CharField(max_length=100, blank=True, null=True, choices=volume_choice)
    volume = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    commodity = models.ForeignKey(Commodity, on_delete=models.SET_NULL, blank=True,
                                  null=True)
    mode = models.ForeignKey(Mode, on_delete=models.SET_NULL, blank=True,
                             null=True)
    carrier = models.ForeignKey(Carrier, on_delete=models.SET_NULL, blank=True,
                                null=True)

    origin = models.ForeignKey(Port, on_delete=models.SET_NULL, blank=True,
                               null=True, related_name='origin_port')
    destination = models.ForeignKey(Port, on_delete=models.SET_NULL, blank=True,
                                    null=True, related_name='destination_port')
