from .base import *

DEBUG = False
ADMINS = (("Antonio M", "email@mydomain.com"),)
ALLOWED_HOSTS = [".educaproject.com"]
DATABASES = {
 'default': {
 'ENGINE': 'django.db.backends.postgresql',
 'NAME': 'educa',
 'USER': 'educa',
 'PASSWORD': 'testpress',
 }
}

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'