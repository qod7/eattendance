from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from reseller.models import Reseller
from useraccounts.forms import GenericUserCreationForm


class AddResellerForm(GenericUserCreationForm):
    """
    Form for adding a new reseller.
    """
    contact = forms.CharField(
        label="Reseller's Contact Number",
        max_length=50,
        widget=forms.TextInput(attrs={'class': "form-control"}),
        required=False
    )

    remarks = forms.CharField(
        max_length=100,
        widget=forms.Textarea(attrs={'class': "form-control"}),
        required=False
    )

    organization_creation_limit = forms.IntegerField(
        help_text="The maximum number of organizations\
             that can be created.",
    )

    class Meta:
        labels = {
            'remarks': "Additional Info",
            'organization_creation_limit': "Organization Limit",
        }
        help_texts = {
            'remarks': 'Optional. For internal use.',
        }

    def save(self):
        """
        Creates the user and saves the reseller from form parameters.
        Sends login credentials in email.
        """
        # create user/send login credentials via email.
        user = super(AddResellerForm, self).save()
        assert user is not None

        # create an organization
        # todo: review pattern for inject user into form in Two Scoops.
        Reseller.objects.create(
            user=user,
            contact=self.cleaned_data.get('contact'),
            remarks=self.cleaned_data.get('remarks'),
            organization_creation_limit=self.cleaned_data.get('organization_creation_limit'),
        )


class ResellerUpdateForm(forms.ModelForm):
    """
    Form for updating a reseller
    """
    class Meta:
        model = Reseller
        fields = ['contact', 'remarks', 'organization_creation_limit']
        widgets = {
            'contact': forms.TextInput(attrs={'class': "form-control"}),
            'remarks': forms.Textarea(attrs={'class': "form-control"}),
            'organization_creation_limit': forms.NumberInput(
                attrs={'class': "form-control"}
            )
        }

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('update', 'Update', css_class='btn-primary'))
        super(ResellerUpdateForm, self).__init__(*args, **kwargs)
