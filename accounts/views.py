from django.views.generic import FormView
from .forms import SignupForm
from django.contrib.auth.views import (LoginView,
	LogoutView,
	PasswordResetView,
	PasswordChangeView,
	PasswordChangeDoneView,
	PasswordResetConfirmView,
	PasswordResetDoneView,
	)


class AccountsSignupView(FormView):
	template_name = "accounts/signup.html"
	form_class = SignupForm



class AccountsLoginView(LoginView):
	template_name = "accounts/login.html"



class AccountsLogoutView(LogoutView):
	next_page = "login"



class AccountsPasswordResetView(PasswordResetView):
	template_name = "accounts/password_reset.html"



class AccountsPasswordChangeView(PasswordChangeView):
	template_name = "accounts/password_change.html"
	success_url = "password_change_done"



class AccountsPasswordChangeDoneView(PasswordChangeDoneView):
	template_name = "accounts/password_change_done.html"



class AccountsPasswordResetConfirmView(PasswordResetConfirmView):
	template_name = "accounts/password_reset_confirm.html"
	success_url = "password_reset_done"



class AccountsPasswordResetDoneView(PasswordResetDoneView):
	template_name = "accounts/password_reset_done.html"
