from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^list-resellers/$', views.ResellerListView.as_view(), name='list_resellers'),
    url(r'^add-reseller/$', views.AddResellerView.as_view(), name='add_reseller'),
    url(r'^settings/$', views.SettingsView.as_view(), name='settings'),
]
