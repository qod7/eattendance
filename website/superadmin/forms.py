from django import forms
from reseller.models import Reseller


class AddResellerForm(forms.ModelForm):

    """
    Form for adding a new reseller.
    """
    first_name = forms.CharField(label='First Name', max_length=30)
    last_name = forms.CharField(label='Last Name', max_length=30)
    email = forms.EmailField()

    class Meta:
        model = Reseller
        fields = ['contact', 'remarks', 'organization_creation_limit']
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

    def save(self):
        # create a user with username = fname_lname
        # check if user is unique and if not, make it unique
        # save first name, last name, email to the user
        # generate a password
        # set this user to the model instance's user object
        # send an email to the user with his credentials
        super(AddResellerForm, self).save()

    # def send_email(self, user, password):
    #     """
    #     Sends an email to the school admin with login credentials
    #     """
    #     from_email = 'Max Connect<maxconnectnepal@gmail.com>'
    #     template_subject = 'reseller/email_templates/subject.txt'
    #     template_html = 'reseller/email_templates/email.html'
    #     template_text = 'reseller/email_templates/email.txt'
    #     subject = get_template(template_subject)
    #     html = get_template(template_html)
    #     text = get_template(template_text)

    #     c = Context({
    #         'user': user,
    #         'password': password,
    #         'name': self.cleaned_data['admin_first_name'] + ' ' + self.cleaned_data['admin_last_name'],
    #     })

    #     subject_content = subject.render(c)
    #     text_content = text.render(c)
    #     html_content = html.render(c)

    #     msg = EmailMultiAlternatives(
    #         subject=subject_content, body=text_content, from_email=from_email, to=[self.cleaned_data['admin_email']])

    #     msg.attach_alternative(html_content, "text/html")
    #     msg.send(fail_silently=True)

    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     if User.objects.filter(username=username).exists():
    #         raise forms.ValidationError('Username "%(value)s" is already in use.',
    #                                     params={'value': username},
    #                                     code='already_exists')
    #     return username

    # def clean_email(self):
    #     username = self.cleaned_data.get('username')
    #     if User.objects.filter(username=username).exists():
    #         raise forms.ValidationError('Username "%(value)s" is already in use.',
    #                                     params={'value': username},
    #                                     code='already_exists')
    #     return email
