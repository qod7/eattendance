from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class ResellerTestMixin(LoginRequiredMixin, UserPassesTestMixin):

    """
    Checks if user is logged in and if user is a reseller.
    """

    def test_func(self):
        # return self.request.user.reseller.exists()
        pass


class HomeView(ResellerTestMixin, TemplateView):
    template_name = "reseller/base.html"
