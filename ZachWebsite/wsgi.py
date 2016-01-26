"""
WSGI config for ZachWebsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

sys.path.append('/zachsite/site/ZachWebsite')
sys.path.append('/zachsite/site')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ZachWebsite.settings")

application = get_wsgi_application()
