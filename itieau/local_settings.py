DEBUG = True

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_ROOT = '/Users/shanecrossan/Sites/itievolution/itieau/static/'

TEMPLATE_DIRS =(
    '/Users/shanecrossan/Sites/itievolution/itieau/itieau/templates',
)