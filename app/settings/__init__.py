import os

# from .local import *
from .beta import *

SECRET_KEY = 'test'
# SECRET_KEY = os.environ.get('SECRET_KEY')

DATABASES['default']['USER']     = os.environ.get('POSTGRES_USER')
DATABASES['default']['PASSWORD'] = os.environ.get('POSTGRES_PASSWORD')

