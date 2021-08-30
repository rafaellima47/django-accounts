from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import User
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3

class AccountsSignupForm(UserCreationForm):
	
	class Meta:
		model = User
		fields = ["email", "password1", "password2"]



class AccountsLoginForm(AuthenticationForm):
	remember_me = forms.BooleanField(initial=True, required=False)
	captcha = ReCaptchaField(required=True)



