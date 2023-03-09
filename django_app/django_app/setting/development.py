from .base import *

SECRET_KEY = "django-insecure-l1gfxh2q8rmw8@gff8gf@-05qu2y6cbjd0w+b0y#f3^(ydpac5"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS += [
    "debug_toolbar",
]
MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]
