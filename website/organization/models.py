from django.db import models
from reseller.models import Reseller

from django.contrib.auth.models import User


class Organization(models.Model):
    """
    A generic organization. From here we can inherit school, bank etc.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField("Name", max_length=100)
    reseller = models.ForeignKey(Reseller, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"

    def __str__(self):
        return self.name
