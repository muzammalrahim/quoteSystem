from django.db import models
from django.utils.translation import ugettext_lazy as _


class Customer(models.Model):
	name = models.CharField(_('name'), max_length=30, null=False, blank=False)
	created_at = models.DateField(blank=True, null=True, auto_now_add=True)
	updated_at = models.DateField(blank=True, null=True, auto_now=True)

	class Meta:
		db_table = 'qms_customer'

	def __str__(self):
		return str(self.name)
