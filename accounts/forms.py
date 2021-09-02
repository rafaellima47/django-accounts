from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms
from django.conf import settings
try:
	from captcha.fields import ReCaptchaField
except:
	pass 


class AccountsSignupForm(UserCreationForm):
	
	class Meta:
		model = get_user_model()
		fields = ["email"]



class AccountsLoginForm(AuthenticationForm):
	remember_me = forms.BooleanField(initial=True, required=False)

	def __init__(self, request=None, *args, **kwargs):
		self.recaptcha()
		super().__init__(self, request=None, *args, **kwargs)

	def recaptcha(self):
		# If django recaptcha is installed creates the captcha field
		if "captcha" in settings.INSTALLED_APPS:
			self.captcha = ReCaptchaField(required=True)

