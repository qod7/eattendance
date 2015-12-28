from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView


def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")


# class HomeView(TemplateView):

#     '''Just to test base.html'''

#     template_name = "layout/dashboard_base/base.html"

class HomeView(RedirectView):

    '''Redirects to the login page'''

    pattern_name = "account:login"


class LoginView(TemplateView):

    '''Just to test base.html'''

    template_name = "useraccounts/login.html"
