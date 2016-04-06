from rest_framework import serializers

from organization.models import Attendance, Staff


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
