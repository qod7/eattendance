from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

from reseller.models import Reseller


class Organization(models.Model):
    """
    A generic organization. From here we can inherit school, bank etc.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='organization')
    name = models.CharField("Name", max_length=100)
    contact = models.CharField("Admin's Contact Number", max_length=50)
    reseller = models.ForeignKey(Reseller, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"
        ordering = ('-user__date_joined',)

    def __str__(self):
        return self.name

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


class Message(models.Model):
    """
    A Message is something sent by the organization to a subset of staff
    """

    title = models.CharField("Title", max_length=50)
    message = models.CharField("Message", max_length=400)
    organization = models.ForeignKey(Organization, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    sent_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"

    def __str__(self):
        return self.title


class Shift(models.Model):
    """
    Defines a Shift for a staff
    """

    name = models.CharField("Name of the Shift", max_length=50)
    on_duty_time = models.TimeField()
    off_duty_time = models.TimeField()
    late_time = models.TimeField()
    leave_early_time = models.TimeField()
    beginning_in = models.TimeField()
    ending_in = models.TimeField()
    beginning_out = models.TimeField()
    ending_out = models.TimeField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    organization = models.ForeignKey(Organization, related_name='shifts', on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Shift"
        verbose_name_plural = "Shifts"

    def __str__(self):
        return self.name


class Staff(models.Model):
    """
    A staff can log in to the android app.
    - is associated with an organization
    - has an ID that can identify org
    - has a date of birth for birthday
    - has a particular shift
    """

    user = models.OneToOneField(User, related_name='staff', on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, related_name='staffs', on_delete=models.CASCADE)
    shifts = models.ManyToManyField(Shift, related_name="staff")
    dob = models.DateField()
    extras = JSONField(null=True, blank=True)
    preferences = JSONField(null=True, blank=True)
    photo = models.ImageField()
    contact = models.CharField("Contact Info", max_length=50, blank=True, default="")

    class Meta:
        verbose_name = "Staff"
        verbose_name_plural = "Staff"

    def __str__(self):
        return self.user.username

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

    def is_present(self, date):
        return Attendance.objects.filter(staff=self, when=date).exists()


class Attendance(models.Model):
    """
    Records a single attendance
    """

    METHOD_CHOICES = (
        (1, 'fingerprint'),
        (2, 'rfid'),
        (3, 'password'),
        (4, 'manual'),
    )

    staff = models.ForeignKey(Staff, related_name='attendances', on_delete=models.CASCADE)
    when = models.DateTimeField(auto_now_add=True)
    method = models.IntegerField(choices=METHOD_CHOICES, default=1)

    class Meta:
        verbose_name = "Attendance"
        verbose_name_plural = "Attendances"

    def __str__(self):
        return self.staff.user.get_full_name()


class Calendar(models.Model):
    """
    Calendar for an organization
    """

    organization = models.OneToOneField(Organization, related_name="calendar", on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Calendar"
        verbose_name_plural = "Calendars"

    def __str__(self):
        return self.organization.name

    def convert_ad_to_bs(self):
        pass

    def convert_bs_to_ad(self):
        pass

    def get_hoildays(self):
        return Event.objects.filter(calendar=self, title__icontains="Holiday")


class Day(models.Model):
    """
    Represents a day in a particular calendar
    """

    date = models.DateField()
    calendar = models.ForeignKey(Calendar)
    holiday = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Day"
        verbose_name_plural = "Days"

    def __str__(self):
        return self.date


class Event(models.Model):
    """
    Stores an event in the calendar.
    """

    title = models.CharField("Title", max_length=50)
    description = models.TextField()
    day = models.ForeignKey(Day)
    # if it's an event that spans multiple days, define end_date as well
    # end_day = models.ForeignKey(Day, null=True)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return self.title
