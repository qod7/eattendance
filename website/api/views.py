from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView)

from organization.models import Notice
from api.serializers import NoticeSerializer
from api.permissions import IsOrganizationOwnerOrReadOnly


class NoticeMixin(object):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    permission_classes = (IsOrganizationOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user


class NoticeList(NoticeMixin, ListCreateAPIView):
    pass


class NoticeDetail(NoticeMixin, RetrieveUpdateDestroyAPIView):
    pass
