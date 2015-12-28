from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from organization.models import Organization


class Staff(models.Model):
    # some sort of ID (15 digit, 5 digit for organization, 5 for user, and 5 random padding for security?)
    # first name
    # last name
    # dob (fo birthday and shit)
    # TODO shift
    # TODO user group
    # password hash
    # Extra Fields (Json string)
    # photo (user id. jpg) (simple af)
    # preferences (for app?)  (should also be a Json String)
    # Organization
    user = models.OneToOneField(User, related_name='staff')
    organization = models.ForeignKey(Organization, related_name='staffs')
    # some sort of ID
    # 15 digit, 5 digit for organization,
    # 5 for user, and 5 random padding for security
    uniqueId = models.CharField("Unique Id", max_length=15)
    dob = models.DateField()
    extras = JSONField()
    preferences = JSONField()
    photo = models.ImageField()

    def __str__(self):
        return self.user.username
