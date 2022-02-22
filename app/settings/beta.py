import os

from .base import *

DEBUG = True
BETA = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_NAME'),
        'HOST': 'db',
        'PORT': '5432'
    }
}
