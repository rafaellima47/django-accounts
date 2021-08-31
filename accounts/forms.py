from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import User
from captcha.fields import ReCaptchaField
from django.forms import ModelForm

class AccountsSignupForm(UserCreationForm):
	
	class Meta:
		model = get_user_model()
		fields = ["email"]

	def save(self, commit=True):
		user = super(AccountsSignupForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		user.email = self.cleaned_data["email"]
		if commit:
			user.save()
		return user
	



class AccountsLoginForm(AuthenticationForm):
	remember_me = forms.BooleanField(initial=True, required=False)
	captcha = ReCaptchaField(required=True)

