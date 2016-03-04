from django import forms

from useraccounts.forms import GenericUserCreationForm
from organization.models import Organization


class AddOrganizationForm(GenericUserCreationForm):

    """
    Form for creating an organization
    1. Take input data: org name, org admin name, email address
    2. creates a user for the organization
    3. creates an organization with user from 2 and current reseller
    4. sends an email to the org admin with login details
    """
    organization_name = forms.CharField(
        label="Name of the Organization",
        max_length=100,
        widget=forms.TextInput(attrs={'class': "form-control"})
    )

    contact = forms.CharField(
        label="Admin's Contact Number",
        max_length=50,
        widget=forms.TextInput(attrs={'class': "form-control"})
    )

    def save(self, reseller):
        """
        Creates the user and saves the organization from form parameters.
        Sends login credentials in email.
        """
        # create user/send login credentials via email.
        user = super(AddOrganizationForm, self).save()
        assert user is not None

        # create an organization
        # todo: review pattern for inject user into form in Two Scoops.
        Organization.objects.create(
            user=user,
            name=self.cleaned_data.get('organization_name'),
            contact=self.cleaned_data.get('contact'),
            reseller=reseller,
        )
