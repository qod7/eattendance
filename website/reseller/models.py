import datetime

from django.db import models
from django.contrib.auth.models import User


def get_default_expiry_date():
    return datetime.datetime.now() + datetime.timedelta(days=365)


class Reseller(models.Model):
    """
    All info and methods pertaining to a reseller
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='reseller')
    # expiry_date = models.DateField(default=get_default_expiry_date)
    contact = models.CharField("Contact Info", max_length=50, blank=True, default="")
    remarks = models.TextField(blank=True, default="")
    organization_creation_limit = models.IntegerField(default=1)

    class Meta:
        verbose_name = "Reseller"
        verbose_name_plural = "Resellers"

    def __str__(self):
        return self.user.get_full_name()

    def organization_count(self):
        """
        Returns the number of organizations created by the reseller
        """
        return self.organization_set.count()

    def can_create_organization(self):
        """
        Can the reseller create an organization?
        """
        if self.organization_count() >= self.organization_creation_limit:
            return False
        return True

    def deactivate_account(self):
        """
        Deactivated accounts get a message at login.
        """
        self.user.is_active = False
        self.user.save()

    def activate_account(self):
        """
        For re-activation.
        """
        self.user.is_active = True
        self.user.save()
