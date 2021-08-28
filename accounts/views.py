from django.views.generic import CreateView
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
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


class AccountsSignupView(CreateView):
	template_name = "registration/signup.html"
	form_class = AccountsSignupForm
	success_url = reverse_lazy("index")
	
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return HttpResponseRedirect(self.get_success_url())
		return super(AccountsSignupView, self).get(request, *args, **kwargs)
	


class AccountsLoginView(LoginView):
	form_class = AccountsLoginForm
	redirect_authenticated_user = True

	def form_valid(self, form):
		if not form.cleaned_data.get("remember_me"):
			self.request.session.set_expiry(0)
		login(self.request, form.get_user())
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

