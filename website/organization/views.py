from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.db.models.fields.related_descriptors import RelatedObjectDoesNotExist

from .models import Organization, Staff, Attendance


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
    """
    Dashboard that shows overall statistics.
    """
    template_name = "organization/dashboard.html"

    def dispatch(self, request, *args, **kwargs):
        self.organization = self.request.user.organization
        return super(HomeView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['title'] = "Dashboard"
        context['staff_count'] = Staff.objects.filter(organization=self.organization).count()
        try:
            Staff.objects.get(organization=self.organization)
        except (Staff.DoesNotExist, Staff.MultipleObjectsReturned):
            context['attendance_count'] = 0
        else:
            context['attendance_count'] = Attendance.objects.filter(staff__organization=self.organization).count()
        return context


class StaffListView(OrganizationTestMixin, ListView):
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

    def get_context_data(self, **kwargs):
        context = super(MessagesView, self).get_context_data(**kwargs)
        context['title'] = "Messages"
        return context


class AnalyticsView(OrganizationTestMixin, TemplateView):
    template_name = "organization/analytics.html"

    def get_context_data(self, **kwargs):
        context = super(AnalyticsView, self).get_context_data(**kwargs)
        context['title'] = "Analytics"
        return context


class SettingsView(OrganizationTestMixin, TemplateView):
    template_name = "organization/settings.html"

    def get_context_data(self, **kwargs):
        context = super(SettingsView, self).get_context_data(**kwargs)
        context['title'] = "Settings"
        return context
