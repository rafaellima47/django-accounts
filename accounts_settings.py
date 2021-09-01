# -------------------- Accounts Settings --------------------

# Sets the accounts User model as deafult auth model
AUTH_USER_MODEL = 'accounts.User'



# Console Email backend (During Development Only)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'



# Email configuration
EMAIL_HOST = ''
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True



# Python Social Auth backends configuration
# Access 'https://python-social-auth.readthedocs.io/en/latest/backends/index.html' for all available backends
SOCIAL_AUTHENTICATION_BACKENDS = []
# Adds SOCIAL_AUTHENTICATION_BACKENDS to global authentication backends variable
settings.AUTHENTICATION_BACKENDS += SOCIAL_AUTHENTICATION_BACKENDS



# Python Social Auth Context Processors
SOCIAL_CONTEXT_PROCESSORS = [
    'social_django.context_processors.backends',
    'social_django.context_processors.login_redirect',
]
# Adds Social Auth context processors to TEMPLATES configuration
TEMPLATES[0]["OPTIONS"]["context_processors"] += SOCIAL_CONTEXT_PROCESSORS



LOGIN_URL = "login"
LOGOUT_URL = "logout"
LOGIN_REDIRECT_URL = "index"



# Sets the session timeout to 1 month (in seconds)
SESSION_COOKIE_AGE = 60 * 60 * 24 * 30 #1 Month



# ReCaptcha keys
RECAPTCHA_PRIVATE_KEY = ""
RECAPTCHA_PUBLIC_KEY = ""



# Password hasher list, with Argon2 as default
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]
