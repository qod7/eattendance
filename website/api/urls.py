from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^notices/$', views.NoticeList.as_view(), name='notice_list'),
    url(r'^notices/(?P<pk>[0-9]+)$', views.NoticeDetail.as_view(), name='notice_detail'),
]
