"""
Django settings for django_app project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!



# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "pages",
    "hosts",
    "images",
    "django.contrib.humanize",
    "django_cleanup.apps.CleanupConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "django_app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "pages.context_processors.global_settings",
            ],
        },
    },
]

WSGI_APPLICATION = "django_app.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "fa-IR"

TIME_ZONE = "Asia/Tehran"

USE_I18N = False
USE_L10N = False
USE_TZ = False


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Setting We Defined
STATICFILES_DIRS = [
    BASE_DIR / "static",
    # '/var/www/static/',
]

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]
STATIC_ROOT = os.path.join(BASE_DIR, "static_root")
STATIC_URL = "/static/"
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "uploads")
# EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
# EMAIL_FILE_PATH = str(BASE_DIR.joinpath("sent_emails"))

SITE_URL = "https://samplesite.ir/"

WHMCS_BASE_URL = "https://samplesite.ir/panel/"
WHMCS_URL = WHMCS_BASE_URL
WHMCS_DOMAIN_SEARCH = WHMCS_BASE_URL + "cart.php"
WHMCS_LOGIN = WHMCS_BASE_URL + "index.php?rp=/login"
WHMCS_SIGHNUP = WHMCS_BASE_URL + "/register.php"
WHMCS_AFFILATE = WHMCS_BASE_URL + "affiliates.php"
WHMCS_TICKET = WHMCS_BASE_URL + "affiliates.php"
LORA_BLOG = "https://samplesite.ir/"
LORA_URL = "https://website.ir/"

LOGGING_LEVEL = "DEBUG"
LOGGING_DIR = "logs"
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file_general": {
            "level": LOGGING_LEVEL,
            "class": "logging.FileHandler",
            "filename": BASE_DIR / LOGGING_DIR / "general.log",
            "formatter": "file",
        },
        "file_app": {
            "level": LOGGING_LEVEL,
            "class": "logging.FileHandler",
            "filename": BASE_DIR / LOGGING_DIR / "app.log",
            "formatter": "file",
        },
        "file_cron": {
            "level": LOGGING_LEVEL,
            "class": "logging.FileHandler",
            "filename": BASE_DIR / LOGGING_DIR / "cron.log",
            "formatter": "file",
        },
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "console",
            "level": LOGGING_LEVEL,
        },
    },
    "formatters": {
        "console": {"format": "%(name)-12s %(levelname)-8s %(message)s"},
        "file": {
            "format": "%(asctime)s %(name)-12s %(filename)-5s %(funcName)-5s %(levelname)-8s %(message)s"
        },
    },
    "loggers": {
        "": {
            "handlers": ["file_general"],
            "level": LOGGING_LEVEL,
        },
        "app": {
            "handlers": ["file_app", "console"],
            "level": LOGGING_LEVEL,
            "propagate": False,
        },
        "cron": {
            "handlers": ["file_cron"],
            "level": LOGGING_LEVEL,
            "propagate": False,
        },
    },
}