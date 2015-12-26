from django.db import models


class Organization(models.Model):
    """
    A generic organization. From here we can inherit school, bank etc.
    """
    name = models.CharField("Name", max_length=100)

    class Meta:
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"

    def __str__(self):
        return self.name
