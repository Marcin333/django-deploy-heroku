import os
from django.conf import settings

PYTHONPATH_SETTINGS = 'ecommerce2.settings'
# specify the name of your settings module
os.environ['DJANGO_SETTINGS_MODULE'] = PYTHONPATH_SETTINGS

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

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR), 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'newsletter.context_processors.condition_all',
            ],
        },
    },
]


STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static', 'static_root')
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static', 'media')

# STATICFILES_DIRS are gonna to go to the STATIC_ROOT after collectstatic
STATICFILES_DIRS = (os.path.join(os.path.dirname(BASE_DIR),'static', 'static_files'),)

