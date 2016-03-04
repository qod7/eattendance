from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.db.models.fields.related_descriptors import RelatedObjectDoesNotExist

from .models import Organization


class OrganizationTestMixin(LoginRequiredMixin, UserPassesTestMixin):

    """
    Checks if user is logged in and if user is a organization.
    """

    def test_func(self):
        try:
            return self.request.user.organization
        except Organization.DoesNotExist:
            return False


class HomeView(OrganizationTestMixin, TemplateView):
    template_name = "organization/dashboard.html"


class StaffListView(OrganizationTestMixin, TemplateView):
    template_name = "organization/list_staff.html"


class MessagesView(OrganizationTestMixin, TemplateView):
    template_name = "organization/messages.html"


class AnalyticsView(OrganizationTestMixin, TemplateView):
    template_name = "organization/analytics.html"


class SettingsView(OrganizationTestMixin, TemplateView):
    template_name = "organization/settings.html"
