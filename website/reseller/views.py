from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Reseller


class ResellerTestMixin(LoginRequiredMixin, UserPassesTestMixin):

    """
    Checks if user is logged in and if user is a reseller.
    """

    def test_func(self):
        # return self.request.user.reseller.exists()
        # todo: find a way to do this using groups
        return Reseller.objects.filter(user=self.request.user).exists()


class HomeView(ResellerTestMixin, TemplateView):
    template_name = "reseller/base.html"
