from django.db import models
from country.models import Port


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
    commodity = models.ForeignKey("mode.Commodity", on_delete=models.SET_NULL, blank=True,
                                  null=True)
    mode = models.ForeignKey("mode.Mode", on_delete=models.SET_NULL, blank=True,
                             null=True)
    carrier = models.ForeignKey("mode.Carrier", on_delete=models.SET_NULL, blank=True,
                                null=True)

    origin = models.ForeignKey(Port, on_delete=models.SET_NULL, blank=True,
                               null=True, related_name='origin_port')
    destination = models.ForeignKey(Port, on_delete=models.SET_NULL, blank=True,
                                    null=True, related_name='destination_port')


class CompanyBaseTariff(models.Model):
    origin = models.ForeignKey(Port, on_delete=models.SET_NULL, blank=True,
                               null=True, related_name='cbt_origin_port')
    destination = models.ForeignKey(Port, on_delete=models.SET_NULL, blank=True,
                                    null=True, related_name='cbt_destination_port')
    mode = models.ForeignKey("mode.Mode", on_delete=models.SET_NULL, blank=True,
                             null=True)
    currency_choice = (
        ('AUD', 'AUD'),
        ('USD', 'USD'),
        ('NZD', 'NZD'),

    )
    currency = models.CharField(max_length=100, blank=True, null=True, choices=currency_choice)
    carrier = models.ForeignKey("mode.Carrier", on_delete=models.SET_NULL, blank=True,
                                null=True)
    srv_lel_choice = (
        ('ROR', 'ROR'),
    )
    srv_lel = models.CharField(max_length=100, blank=True, null=True, choices=srv_lel_choice)
    comment_choice = (
        ('MVEH', 'MVEH'),
        ('MBIK', 'MBIK'),
    )
    comment = models.TextField(max_length=200, blank=True, null=True, choices=comment_choice)

    unit_choice = (
        ('M3', 'M3'),
        ('M2', 'M2'),
        ('M1', 'M1'),
    )
    unit_type = models.CharField(max_length=100, blank=True, null=True, choices=unit_choice)
    frequency_choice = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),

    )
    frequency = models.CharField(max_length=100, blank=True, null=True, choices=frequency_choice)
    frequency_unit_choice = (
        ('Fortnight', 'Fortnight'),
        ('Monthly', 'Monthly'),
    )
    frequency_unit = models.CharField(max_length=100, blank=True, null=True, choices=frequency_unit_choice)
    start_date = models.DateField(blank=True, null=True, auto_now_add=True)
    # charge_code = models.ForeignKey(ChargeCode, on_delete=models.SET_NULL, blank=True, null=True)

    # def save(self,*args,**kwargs):
    #     if not self.id:
    #         self.start_date = timezone.now()
    #     return super(CompanyBaseTariff, self).save(*args, **kwargs)
