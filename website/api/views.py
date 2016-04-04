import logging

from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from organization.models import Staff
from .serializers import AttendanceSerializer, StaffSerializer


logger = logging.getLogger('django_debug')


class SaveAttendance(generics.CreateAPIView):
    """Save received attendance"""

    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]

    def post(self, request, *args, **kwargs):
        logger.debug('Received request for attendance')


class StaffViewSet(viewsets.ModelViewSet):
    """DRF viewset for CRUD operation of staffs."""

    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    authentication_classes = [TokenAuthentication, ]
