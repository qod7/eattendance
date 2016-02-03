from rest_framework import serializers

from organization.models import Notice


class NoticeSerializer(serializers.ModelSerializer):
    organization = serializers.Field('organization.user.username')

    class Meta:
        model = Notice
        fields = ('message', 'sentOn', 'organization')
