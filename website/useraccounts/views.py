from django.shortcuts import render, redirect
from django.views.generic import View

from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

from reseller.models import Reseller
from organization.models import Organization


class LoginView(View):

    '''
    View for logging in a user.
    '''

    def get(self, request):
        if request.user.is_authenticated():
            return self.check_user_type_and_redirect(request)

        return render(self.request, 'useraccounts/login.html', {'title': 'Login'})

    def post(self, request):
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
            messages.error(self.request, "Invalid username or password.")
            return redirect('account:login')

    def check_user_type_and_redirect(self, request):
        '''
        check whether the user is a superadmin, reseller, or organization
        and redirect them to their respective dashboard
        '''
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
