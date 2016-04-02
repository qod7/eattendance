from django.shortcuts import render, redirect
from django.views.generic import View

from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode

from reseller.models import Reseller
from organization.models import Organization


class LoginView(View):
    """
    View for logging in a user.
    """

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return self.check_user_type_and_redirect(request)

        return render(self.request, 'useraccounts/login.html', {'title': 'Login'})

    def post(self, request, *args, **kwargs):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                auth.login(self.request, user)
                return self.check_user_type_and_redirect(self.request)
            else:
                messages.error(
                    self.request,
                    "Sorry, your account has been deactivated.\
                     Please contact the administrator.")
                return redirect('account:login')
        else:
            messages.error(self.request, "Invalid username or password."
                           " Note that both fields may be case-sensitive.")
            return redirect('account:login')

    def check_user_type_and_redirect(self, request):
        """
        Check whether the user is a superadmin, reseller, or organization
        and redirect them to their respective dashboard
        """
        if request.user.is_staff:
            return redirect('superadmin:home')
        elif Reseller.objects.filter(user=request.user).exists():
            return redirect('reseller:home')
        elif Organization.objects.filter(user=request.user).exists():
            return redirect('organization:home')
        else:
            auth.logout(request)
            messages.error(self.request,
                           "Your account has been deleted.\
                            Please contact the administrator.")
            return redirect('account:login')


@login_required(login_url='account:login')
def logout(request):
    auth.logout(request)
    return redirect('account:login')


class ResetPasswordView(View):
    """
    Resets password
    """

    def post(self, request, *args, **kwargs):
        """
        Takes email and puts it into password reset form.
        """
        form = PasswordResetForm(request.POST)
        from_email = None
        email_template_name = 'useraccounts/password_reset/password_reset_email.txt'
        html_email_template_name = 'useraccounts/password_reset/password_reset_email.html'
        subject_template_name = 'useraccounts/password_reset/password_reset_subject.txt'
        extra_email_context = {}

        if form.is_valid():
            opts = {
                'use_https': request.is_secure(),
                'token_generator': default_token_generator,
                'from_email': from_email,
                'email_template_name': email_template_name,
                'subject_template_name': subject_template_name,
                'request': self.request,
                'html_email_template_name': html_email_template_name,
                'extra_email_context': extra_email_context,
            }

            form.save(**opts)

        messages.success(
            request, "We've emailed you instructions for resetting your password.\
             You should be receiving them shortly.")
        return redirect('account:login')


def password_reset_confirm(request, uidb64=None, token=None):
    """
    View that checks the hash in a password reset link and presents a
    form for entering a new password.
    """
    UserModel = auth.get_user_model()
    assert uidb64 is not None and token is not None  # checked by URLconf

    try:
        # urlsafe_base64_decode() decodes to bytestring on Python 3
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = UserModel._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        validlink = True
        title = 'Reset Password'

        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your password has been reset successfully.")
                return redirect("account:login")
        else:
            form = SetPasswordForm(user)
    else:
        validlink = False
        form = None
        title = 'Password reset unsuccessful'

    context = {
        'form': form,
        'title': title,
        'validlink': validlink,
    }

    return render(request, 'useraccounts/password_reset/password_reset_confirm.html', context)
