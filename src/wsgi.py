# import os
# import sys

# from os.path import dirname, realpath
# from site import addsitedir

# BASE_DIR = dirname(realpath(__file__))

# WORKON_HOME = os.environ['WORKON_HOME']
# VENV = 'django_1_7'

# addsitedir('{0}/{1}/lib/python2.7/site-packages'.format(WORKON_HOME, VENV))

# sys.path = [BASE_DIR] + sys.path

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.production')

# # activamos el entorno virtual
# activate_this = os.path.expanduser(
#     '{0}/{1}/bin/activate_this.py'.format(WORKON_HOME, VENV))
# execfile(activate_this, dict(__file__=activate_this))

# from django.core.wsgi import get_wsgi_application

# application = get_wsgi_application()
"""
WSGI config for base_1_9 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.base")

application = get_wsgi_application()
