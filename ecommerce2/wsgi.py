"""
WSGI config for ecommerce2 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
PYTHONPATH_SETTINGS = 'ecommerce2.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", PYTHONPATH_SETTINGS)
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()
application = DjangoWhiteNoise(application)

