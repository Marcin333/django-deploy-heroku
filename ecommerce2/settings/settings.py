import os
from django.conf import settings

# PYTHONPATH_SETTINGS = 'ecommerce2.settings'
# # specify the name of your settings module
# os.environ['DJANGO_SETTINGS_MODULE'] = PYTHONPATH_SETTINGS

DATABASES = settings.DATABASES

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = False
SECRET_KEY = os.environ['SECRET_KEY'] 

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'



