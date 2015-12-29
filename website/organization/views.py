from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Organization


class OrganizationTestMixin(LoginRequiredMixin, UserPassesTestMixin):

    """
    Checks if user is logged in and if user is a organization.
    """

    def test_func(self):
        # return self.request.user.organization.exists()
        # todo: find a way to do this using groups
        return Organization.objects.filter(user=self.request.user).exists()


class HomeView(OrganizationTestMixin, TemplateView):
    template_name = "organization/base.html"
