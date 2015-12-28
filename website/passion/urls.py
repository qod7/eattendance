from django.conf.urls import url, include
from django.contrib import admin

from . import views

from reseller import urls as reseller_urls
from organization import urls as organization_urls
from api import urls as api_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^reseller/', include(reseller_urls, namespace='reseller')),
    url(r'^organization/', include(organization_urls, namespace='organization')),
    url(r'^api/', include(api_urls, namespace='api')),

    url(r'^$', views.LoginView.as_view(), name='home'),
    url(r'^(?P<filename>(robots.txt)|(humans.txt))$',
        views.home_files, name='home-files'),
]
