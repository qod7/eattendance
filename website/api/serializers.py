from django.contrib.auth.models import User

from rest_framework import serializers

from organization.models import Attendance, Staff


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff

    user = UserSerializer()
