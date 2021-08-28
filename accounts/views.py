from django.views.generic import FormView
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import login as auth_login
from .forms import (
	AccountsSignupForm, 
	AccountsLoginForm
	)
from django.contrib.auth.views import (
	LoginView,
	LogoutView,
	PasswordResetView,
	PasswordChangeView,
	PasswordChangeDoneView,
	PasswordResetConfirmView,
	PasswordResetDoneView,
	PasswordResetCompleteView,
	)


class AccountsSignupView(FormView):
	template_name = "registration/signup.html"
	form_class = AccountsSignupForm



class AccountsLoginView(LoginView):
	form_class = AccountsLoginForm

	def form_valid(self, form):
		if not form.cleaned_data.get("remember_me"):
			self.request.session.set_expiry(0)
			
		auth_login(self.request, form.get_user())
		return HttpResponseRedirect(self.get_success_url())



class AccountsLogoutView(LogoutView):
	pass



class AccountsPasswordResetView(PasswordResetView):
	pass



class AccountsPasswordChangeView(PasswordChangeView):
	pass



class AccountsPasswordChangeDoneView(PasswordChangeDoneView):
	pass



class AccountsPasswordResetConfirmView(PasswordResetConfirmView):
	pass



class AccountsPasswordResetDoneView(PasswordResetDoneView):
	pass



class AccountsPasswordResetCompleteView(PasswordResetCompleteView):
	pass

