from django.contrib import admin

from .models import Organization, Message, Shift, Staff, Attendance
from .models import Calendar, Day, Event

admin.site.register(Organization)
admin.site.register(Message)
admin.site.register(Shift)
admin.site.register(Staff)
admin.site.register(Attendance)
admin.site.register(Calendar)
admin.site.register(Day)
admin.site.register(Event)
