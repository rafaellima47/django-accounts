from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import User


class AccountsSignupForm(UserCreationForm):
	
	class Meta:
		model = User
		fields = ["email", "password1", "password2"]



class AccountsLoginForm(AuthenticationForm):
	remember_me = forms.BooleanField(initial=True, required=False)


