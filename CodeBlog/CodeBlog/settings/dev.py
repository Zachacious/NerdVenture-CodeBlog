# from .base import *
from .pipelineConf_dev import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e&f-k1hb94gd2f9qhik1dc8dc)_$kj72e07+2xf+&h$0l!ej*q'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_MESSAGES_RECEIVER = 'zach@site.com'

MESSAGE_LEVEL = 10

try:
    from .local import *
except ImportError:
    pass
 
WAGTAIL_CACHE = False

NEWSLETTER_FROM_EMAIL = 'Zach@Zach.com'

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = 'localhost:8000'