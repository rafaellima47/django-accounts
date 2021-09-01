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
    
Move the "accounts" folder and accounts_requirements.txt to your project directory.
    
Install the app dependencies:

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

Paste the content of accounts_settings.py to settings.py of your project.

Add your ReCaptcha keys to the settings:

```python
# ReCaptcha keys
RECAPTCHA_PRIVATE_KEY = "Your Private Key"
RECAPTCHA_PUBLIC_KEY = "Your Public Key"
```

Set the backends and the keys of you choice to use with Python Social Auth:

```python
# Python Social Auth backends configuration
SOCIAL_AUTHENTICATION_BACKENDS = [
	'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
]

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'Your google oauth2 key'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'You google oauth2 secret'

SOCIAL_AUTH_TWITTER_KEY = 'Your twitter key'
SOCIAL_AUTH_TWITTER_SECRET = 'Your twitter secret'
```

Make and apply the migrations:

    $ python manage.py makemigrations
    $ python manage.py migrate 


