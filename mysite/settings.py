"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import django
from django.utils.encoding import force_str
django.utils.encoding.force_text = force_str

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "p#dw566&a7f70whcd*$7k9cthul*pshe$xzd-+fiz)^lulf*=@"
OMEGA = BASE_DIR
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['.vercel.app','now.sh','127.0.0.1','localhost']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "main_app.apps.MainAppConfig",
    # social auth apps
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    # provider: Google
    "allauth.socialaccount.providers.google",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware"
]

ROOT_URLCONF = "mysite.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "mysite.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
]

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

EMAIL_HOST = "localhost"
EMAIL_PORT = 587
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = "RESCUE <no-reply@rescue.com>"
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/static/"
MEDIA_URL = "/media/"

if DEBUG:

    STATICFILES_DIRS = [os.path.join(BASE_DIR + "/main_app/", "static")]

else:

    STATIC_ROOT = os.path.join(BASE_DIR + "/main_app/", "static")


MEDIA_ROOT = [os.path.join(BASE_DIR + "/main_app/", "media")]


# SMTP Configuration
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "nbtaylor1031@gmail.com"  # eg : rescue@gmail.com
EMAIL_HOST_PASSWORD = "fxmbvhcyrulpxkvs"  # eg : 213@Hupo34$19wed
DEFAULT_FROM_EMAIL = "nbtaylor1031@gmail.com"


# AUTHENTICATION SETUP
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

SITE_ID = 1
LOGIN_REDIRECT_URL = "/"

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
    }
}


...

# SECURITY WARNING: keep the secret key used in production secret!
...
GOOGLE_RECAPTCHA_SITE_KEY = '6LcYNF4pAAAAAMWWGWZZcgniuFINfhCe528msevr' #your reCAPTCHA SITE key 
# GOOGLE_RECAPTCHA_SITE_KEY = '6LfGawkbAAAAAEwMU9ElnUNXMSG5Az8uXGLRvXZs' #your reCAPTCHA SITE key 


GOOGLE_RECAPTCHA_SECRET_KEY = '6LcYNF4pAAAAAHaH322oTPLYM2-o_ojtHBgJvvYA' #your reCAPTCHA SECRET key 
# GOOGLE_RECAPTCHA_SECRET_KEY = '6LfGawkbAAAAAEXmouoGwTWgBV2__O-2lbOcN9iF' #your reCAPTCHA SECRET key 

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
# STATICFILES_DIRS = [os.path.join(BASE_DIR + "/main_app/", "static")]
# STATIC_ROOT = os.path.join(BASE_DIR + "/main_app/", "static")
...
# 6LfRKF4pAAAAALTKbZFMB22_J7FfHIqNjwqDo49t
# 6LfRKF4pAAAAAOBTt5Wrw4HZR64Cidujg_gUz0Ow