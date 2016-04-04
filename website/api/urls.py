from django.conf.urls import url

from rest_framework import routers

from .views import SaveAttendance, StaffViewSet

router = routers.SimpleRouter()
router.register(r'staff', StaffViewSet)

urlpatterns = [
    url(r'^attendance/', SaveAttendance.as_view(), name='attendance')
] + router.urls
