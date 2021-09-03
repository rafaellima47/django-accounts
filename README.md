# django-accounts
Customizable Django authentication app, with ReCapctha, Python Social Auth and Argon2 as Default password hasher

## Fatures
- [x] Default authentication with email instead of username
- [x] Social auth
- [x] ReCaptcha field/widget
- [x] "Remember me" functionality
- [x] Argon2 as default password hasher

## Built with
- [Python 3](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Python Social Auth](https://python-social-auth.readthedocs.io/en/latest/)
- [Django ReCapctha](https://pypi.org/project/django-recaptcha/)

## Usage
First clone the repository:

    $ git clone git@github.com:rafaellima47/django-accounts.git
    
Move the ``"accounts"`` folder and ``accounts_requirements.txt`` to your project directory.

Now include the accounts urls to ``urls.py`` in your project directory:

```python
urlpatterns = [
	...,
	path("accounts/", include("accounts.urls")),
	...,
]
```
    
Install the app requirements:

    $ pip install -r accounts_requirements.txt
    

Add the following apps to the INSTALLED_APPS in your project settings:

```python
INSTALLED_APPS = [
	...,
	'accounts',
	'captcha',
	'social_django',
	...,
]
``` 

Paste the content of accounts_settings.py to settings.py of your project and configure according to what you will use in your project

Apply the migrations:

    $ python manage.py migrate 

You can now use and customize the app the way you want in your application.
