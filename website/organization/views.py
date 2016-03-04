from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.db.models.fields.related_descriptors import RelatedObjectDoesNotExist

from .models import Organization, Staff


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

    """
    Lists the current staff
    """

    context_object_name = 'staff_list'
    template_name = "organization/list_staff.html"

    def dispatch(self, request, *args, **kwargs):
        self.organization = self.request.user.organization
        return super(StaffListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(StaffListView, self).get_context_data(**kwargs)
        context['title'] = "List Staff"
        return context

    def get_queryset(self):
        return Staff.objects.select_related('user').filter(organization=self.organization)


class MessagesView(OrganizationTestMixin, TemplateView):
    template_name = "organization/messages.html"


class AnalyticsView(OrganizationTestMixin, TemplateView):
    template_name = "organization/analytics.html"


class SettingsView(OrganizationTestMixin, TemplateView):
    template_name = "organization/settings.html"
