from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^list-organizations/$', views.ListOrganizationsView.as_view(), name='list_organizations'),
    url(r'^add-organization/$', views.AddOrganizationsView.as_view(), name='add_organization'),
    url(r'^settings/$', views.SettingsView.as_view(), name='settings'),
]
