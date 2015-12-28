from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

from reseller.models import Reseller


METHOD_CHOICES = (
    (1, 'fingerprint'),
    (2, 'rfid'),
    (3, 'password'),
    (4, 'manual'),
)


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


class Notice(models.Model):
    # id
    # sender id
    # receiver id
    # message
    # sent on (date/time)
    # replied to (is the id of some other notice or null)
    # Organisation
    message = models.CharField("Message", max_length=400)
    organization = models.ForeignKey(Organization, related_name='notices')
    sentOn = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Notice"
        verbose_name_plural = "Notices"

    def __str__(self):
        return self.message


class Shift(models.Model):
    checkIn = models.TimeField()
    checkOut = models.TimeField()

    class Meta:
        verbose_name = "Shift"
        verbose_name_plural = "Shifts"

    def __str__(self):
        pass


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


class Attendance(models.Model):
    staff = models.ForeignKey(Staff, related_name='attendances')
    when = models.DateTimeField(auto_now_add=True)
    method = models.IntegerField(choices=METHOD_CHOICES, default=1)

    class Meta:
        verbose_name = "Attendance"
        verbose_name_plural = "Attendances"

    def __str__(self):
        return self.staff.username
