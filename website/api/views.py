import logging

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import AttendanceSerializer


logger = logging.getLogger('django_debug')


class SaveAttendance(generics.CreateAPIView):
    """Save received attendance"""

    serializer_class = AttendanceSerializer
    # permission_classes = [IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        logger.debug('Received request')
