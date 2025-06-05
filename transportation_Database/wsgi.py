"""
WSGI config for transportation_Database project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os #to interact with environment variables and system settings

from django.core.wsgi import get_wsgi_application #Django function to create a WSGI-compatible application

#default settings module that Django will use to load configurations
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'transportation_Database.settings')

#the WSGI application object that the web server will use to serve your project
application = get_wsgi_application()
