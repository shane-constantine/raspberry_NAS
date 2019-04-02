"""
WSGI config for raspberry_NAS project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file_page, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'raspberry_NAS.settings')

application = get_wsgi_application()
