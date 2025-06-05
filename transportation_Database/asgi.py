"""
ASGI config for transportation_Database project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os #allows to interact with environment variables and system-level settings

from django.core.asgi import get_asgi_application #function that creates an ASGI-compliant Django application

#tell Django which settings module to use
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'transportation_Database.settings')

#create the ASGI application instance that your ASGI server will use
#this acts as the entry point for asynchronous communication
application = get_asgi_application()
