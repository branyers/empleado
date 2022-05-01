from .BASE import *
import os
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempleado',
        'USER': 'branyes',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
# # STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = '/static/'
STATICFILES_DIRS = ['static']


MEDIA_ROOT = BASE_DIR / 'media/'
MEDIA_URL = '/media/'



