from django.shortcuts import render
from django.views.generic import TemplateView


def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")


class HomeView(TemplateView):

    '''Just to test base.html'''

    template_name = "layout/base.html"


class LoginView(TemplateView):

    '''Just to test base.html'''

    template_name = "useraccounts/login.html"
