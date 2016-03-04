from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^list-staff/$', views.StaffListView.as_view(), name='list_staff'),
    url(r'^messages/$', views.MessagesView.as_view(), name='messages'),
    url(r'^analytics/$', views.AnalyticsView.as_view(), name='analytics'),
    url(r'^settings/$', views.SettingsView.as_view(), name='settings'),
]
