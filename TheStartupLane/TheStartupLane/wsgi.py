"""
WSGI config for TheStartupLane project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
sys.path.append('/opt/python/current/app/')


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TheStartupLane.settings")
# os.environ["DJANGO_SETTINGS_MODULE"] = "TheStartupLane.settings"

application = get_wsgi_application()
