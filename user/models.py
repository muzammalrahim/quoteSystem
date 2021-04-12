from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    created_at = models.DateField(blank=True, null=True,auto_now_add=True)
    updated_at = models.DateField(blank=True, null=True,auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = 'qms_user'

    def __str__(self):
        return str(self.email)

