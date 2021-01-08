"""
WSGI config for jgk project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append("/var/www/html/django/jgk/")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jgk.settings')

application = get_wsgi_application()


"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jgk.settings')

application = get_wsgi_application()
"""
