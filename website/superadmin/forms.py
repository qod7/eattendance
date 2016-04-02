from django import forms
from django.contrib.auth.models import User

# for email
from django.core.mail import EmailMultiAlternatives  # , get_connection
from django.template.loader import get_template
from django.template import Context
# end

from reseller.models import Reseller


class AddResellerForm(forms.ModelForm):
    """
    Form for adding a new reseller.
    """
    first_name = forms.CharField(
        label='First Name',
        max_length=30,
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    last_name = forms.CharField(
        label='Last Name',
        max_length=30,
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': "form-control"})
    )

    class Meta:
        model = Reseller
        fields = ['first_name', 'last_name', 'email', 'contact', 'remarks', 'organization_creation_limit']
        labels = {
            'remarks': "Additional Info",
            'organization_creation_limit': "Organization Limit",
        }
        help_texts = {
            'remarks': 'Optional. For internal use.',
            'organization_creation_limit': "The maximum number of organizations\
             that can be created.",
        }
        error_messages = {
            'first_name': {
                'max_length': "First name is too long.",
            },

            'last_name': {
                'max_length': "Last name is too long.",
            },
        }
        widgets = {
            'contact': forms.TextInput(
                attrs={'class': "form-control"}
            ),
            'remarks': forms.Textarea(
                attrs={'class': "form-control"}
            ),
            # 'organization_creation_limit': forms.TextInput(
            #     attrs={'class': "form-control"}
            # )
        }

    def clean_username(self, username):
        # check if user is unique and if not, make it unique
        while User.objects.filter(username=username).exists():
            username = username + '1'
        return username

    def save(self, commit=False):
        """
        Creates the user and saves the reseller from form parameters.
        Sends login credentials in email.
        """
        # get the reseller data from the form
        reseller = super(AddResellerForm, self).save(commit=False)

        # get form parameters
        first_name = self.cleaned_data.get('first_name').lower()
        last_name = self.cleaned_data.get('last_name').lower()
        email = self.cleaned_data.get('email').lower()

        # generate a password
        password = User.objects.make_random_password()

        # create a user with username = fname_lname
        username = self.clean_username(first_name + '_' + last_name)

        # save first name, last name, email to the user
        user = User.objects.create_user(username, email, password)
        user.first_name = first_name.title()
        user.last_name = last_name.title()
        user.save()

        # send an email to the user with his credentials
        self.send_email(user, password)

        # set this user to the model instance's user object
        reseller.user = user
        reseller.save()

        super(AddResellerForm, self).save(commit=True)

    def send_email(self, user, password):
        """
        Sends an email to the reseller with their login credentials
        """
        from_email = 'Passion Technologies<passion@gmail.com>'
        template_subject = 'useraccounts/email_templates/subject.txt'
        template_html = 'useraccounts/email_templates/email.html'
        template_text = 'useraccounts/email_templates/email.txt'
        subject = get_template(template_subject)
        html = get_template(template_html)
        text = get_template(template_text)

        c = Context({
            'user': user,
            'password': password,
            'name': self.cleaned_data['first_name'] + ' ' + self.cleaned_data['last_name'],
        })

        subject_content = subject.render(c)
        text_content = text.render(c)
        html_content = html.render(c)

        msg = EmailMultiAlternatives(
            subject=subject_content, body=text_content, from_email=from_email, to=[self.cleaned_data['email']])

        msg.attach_alternative(html_content, "text/html")
        msg.send(fail_silently=True)

    def clean_email(self):
        """
        Makes sure that user with the same email address does not already exist.
        """
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email address "%(value)s" is already in use.',
                                        params={'value': email},
                                        code='already_exists')
        return email
