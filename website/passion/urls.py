from django.conf.urls import url, include
from django.contrib import admin

from . import views

from reseller import urls as reseller_urls
from organization import urls as organization_urls
from superadmin import urls as superadmin_urls
from api import urls as api_urls
from useraccounts import urls as account_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^accounts/', include(account_urls, namespace='account')),
    url(r'^reseller/', include(reseller_urls, namespace='reseller')),
    url(r'^organization/', include(organization_urls, namespace='organization')),
    url(r'^superadmin/', include(superadmin_urls, namespace='superadmin')),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(api_urls, namespace='api')),

    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^(?P<filename>(robots.txt)|(humans.txt))$',
        views.home_files, name='home-files'),
]
