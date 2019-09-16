from .base import *
from .pipelineConf_Prod import *
import os

from dotenv import load_dotenv
# project_folder = os.path.expanduser('~/NerdVenture-CodeBlog')  # adjust as appropriate
load_dotenv(os.path.join(PROJECT_DIR, '.env'))

DEBUG = False

MESSAGE_LEVEL = 20

SECRET_KEY = os.getenv('SECRET_KEY')

try:
    from .local import *
except ImportError:
    pass

apps = [
    # 'manifesto',

    'wagtail.contrib.frontend_cache',
]

INSTALLED_APPS = apps + INSTALLED_APPS

WAGTAIL_CACHE = True

NEWSLETTER_FROM_EMAIL = 'Zach@NerdVenture.Net'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_MESSAGES_RECEIVER = 'zach@NerdVenture.Net'
EMAIL_SUBJECT_PREFIX = "[NerdVenture] "
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

WAGTAILFRONTENDCACHE = {
    'cloudflare': {
        'BACKEND': 'wagtail.contrib.frontend_cache.backends.CloudflareBackend',
        'EMAIL': 'back4moore@gmail.com',
        'TOKEN': 'gCpbxD4ii8u-1QLdSO36dJtHesBmbz0t8KhVA622',
        'ZONEID': 'f3420199adb7a885e8a5cf55654e1a12',
    },
}

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = 'https://www.nerdventure.com'

ALLOWED_HOSTS = ['www.nerdventure.net', 'nerdventure.net'] 

# STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
STATICFILES_STORAGE = 'CodeBlog.storage.GZIPManifestStorage'

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# keep db connection open longer to increase performance when multiple db calls are needed
CONN_MAX_AGE = 30 # seconds