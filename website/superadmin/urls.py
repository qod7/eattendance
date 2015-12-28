from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^list-resellers/$', views.ListResellersView.as_view(), name='list_resellers'),
    url(r'^create-reseller/$', views.CreateResellerView.as_view(), name='create_reseller'),
    url(r'^settings/$', views.SettingsView.as_view(), name='settings'),
]
