from django.conf.urls import url

from api.views import SaveAttendance


urlpatterns = [
    url(r'^attendance/', SaveAttendance.as_view(), name='attendance')
]
