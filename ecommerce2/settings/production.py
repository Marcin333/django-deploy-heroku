from django.conf import settings
import os

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
TEMPLATE_DEBUG = True


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


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
# urls for static files and media
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static', 'static_root')
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static', 'media')

# STATICFILES_DIRS are gonna to go to the STATIC_ROOT after collectstatic
STATICFILES_DIRS = (os.path.join(os.path.dirname(BASE_DIR),'static', 'static_files'),)

CRISPY_TEMPLATE_PACK = 'bootstrap3'
CRISPY_CLASS_CONVERTERS = {'textinput': "textinput inputtext"}
CRISPY_FAIL_SILENTLY = not DEBUG

# Email setup
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'kmarcin827@gmail.com'
EMAIL_HOST_PASSWORD = 'qawsedrf!'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# Redux registration
DEFAULT_FROM_EMAIL = "<kmarcin827@gmail.com>"
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
SITE_ID = 1


# Braintree settings

BRAINTREE_PUBLIC = '76f8d4y4vtzrdy9z'
BRAINTREE_PRIVATE = 'd408523feca4e8dfd63f8e01972055a2'
BRAINTREE_MERCHANT_ID = '8kqgzwy8xhpmk5zy'
BRAINTREE_ENVIRONMENT = 'Sandbox'