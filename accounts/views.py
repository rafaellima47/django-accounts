from django.views.generic import FormView
from .forms import SignupForm
from django.contrib.auth.views import (LoginView,
										LogoutView,
										)


class AccountsSignupView(FormView):
	template_name = "accounts/signup.html"
	form_class = SignupForm



class AccountsLoginView(LoginView):
	template_name = "accounts/login.html"



class AccountsLogoutView(LogoutView):
	next_page = "login"