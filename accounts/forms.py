from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms


class AccountsSignupForm(UserCreationForm):
	
	class Meta:
		model = get_user_model()
		fields = ["email", "password1", "password2"]



class AccountsLoginForm(AuthenticationForm):
	remember_me = forms.BooleanField(initial=True, required=False)


