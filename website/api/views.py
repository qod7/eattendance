import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from organization.models import Staff, Attendance
from .serializers import StaffSerializer


logger = logging.getLogger('django_debug')


class SaveAttendance(generics.CreateAPIView):
    """API for handling attendance."""

    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]

    def create(self, request):
        """Save received attendance."""

        # Check if keys are present
        keys = ['staff', 'when', 'method']
        for key in keys:
            if(not(key in request.data)):
                data = {
                    'detail': "Missing data '{}' in post request".format(key)
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

        staff_id = request.data['staff']
        when = request.data['when']
        method = request.data['method']

        try:
            staff = Staff.objects.get(pk=staff_id)
        except Staff.DoesNotExist:
            data = {
                'detail': "Staff with given id not found"
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        attendance = Attendance.objects.create(
            staff=staff,
            when=when,
            method=method
        )

        attendance.save()

        return Response({})


class StaffViewSet(viewsets.ModelViewSet):
    """DRF viewset for CRUD operation of staffs."""

    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    authentication_classes = [TokenAuthentication, ]

    def create(self, request):
        logger.debug(request.data)
