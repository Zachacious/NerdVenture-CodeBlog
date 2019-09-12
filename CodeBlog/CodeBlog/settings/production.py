from .base import *
from .pipelineConf_Prod import *
import os

DEBUG = False

MESSAGE_LEVEL = 20

SECRET_KEY = os.getenv('SECRET_KEY')

try:
    from .local import *
except ImportError:
    pass

apps = [
    'manifesto',

    # 'wagtail.contrib.frontend_cache',
]

INSTALLED_APPS = apps + INSTALLED_APPS

WAGTAIL_CACHE = True

NEWSLETTER_FROM_EMAIL = 'Zach@Zach.com'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_MESSAGES_RECEIVER = 'zach@site.com'

# WAGTAILFRONTENDCACHE = {
#     'cloudflare': {
#         'BACKEND': 'wagtail.contrib.frontend_cache.backends.CloudflareBackend',
#         'EMAIL': 'your-cloudflare-email-address@example.com',
#         'TOKEN': 'your cloudflare api token',
#         'ZONEID': 'your cloudflare domain zone id',
#     },
# }

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = 'https://www.nerdventure.com'

ALLOWED_HOSTS = ['www.nerdventure.net', 'nerdventure.net'] 

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'