from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.db.models.fields.related_descriptors import RelatedObjectDoesNotExist


class OrganizationTestMixin(LoginRequiredMixin, UserPassesTestMixin):

    """
    Checks if user is logged in and if user is a organization.
    """

    def test_func(self):
        try:
            return self.request.user.organization
        # except RelatedObjectDoesNotExist:
        except:
            return False


class HomeView(OrganizationTestMixin, TemplateView):
    template_name = "organization/base.html"
