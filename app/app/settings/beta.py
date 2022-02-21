
from .base import *

DEBUG = True
BETA = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'users',
        'HOST': '',
        'PORT': '5432'
    }
}
