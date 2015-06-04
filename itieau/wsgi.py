"""
WSGI config for itieau project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import StringIO
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "itieau.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

def django_application(environ, start_response):

    if environ.get("mod_wsgi.input_chunked") == 1:
        stream = environ["wsgi.input"]
        data = stream.read()
        environ["CONTENT_LENGTH"] = str(len(data))
        environ["wsgi.input"] = StringIO.StringIO(data)

    return application(environ, start_response)