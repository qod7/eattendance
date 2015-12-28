from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class SuperAdminTestMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_staff


class HomeView(LoginRequiredMixin, SuperAdminTestMixin, TemplateView):
    template_name = "superadmin/dashboard.html"


class ListResellersView(LoginRequiredMixin, SuperAdminTestMixin, TemplateView):
    template_name = "superadmin/list_resellers.html"


class CreateResellerView(LoginRequiredMixin, SuperAdminTestMixin, TemplateView):
    template_name = "superadmin/create_reseller.html"


class SettingsView(LoginRequiredMixin, SuperAdminTestMixin, TemplateView):
    template_name = "superadmin/settings.html"
