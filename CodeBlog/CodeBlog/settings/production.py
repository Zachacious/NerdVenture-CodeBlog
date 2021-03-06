from .base import *
# from .pipelineConf_Prod import *
import os

from dotenv import load_dotenv
load_dotenv(os.path.join(PROJECT_DIR, '.env'))

DEBUG = False

MESSAGE_LEVEL = 20

SECRET_KEY = os.getenv('SECRET_KEY')

apps = [
    # 'manifesto',

    'wagtail.contrib.frontend_cache',
    # 'wagalytics',
]

INSTALLED_APPS = INSTALLED_APPS + apps

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

GA_KEY_FILEPATH = os.getenv('GA_KEY_FILEPATH')
GA_VIEW_ID = os.getenv('GA_VIEW_ID')

WAGTAILFRONTENDCACHE = {
    'cloudflare': {
        'BACKEND': 'wagtail.contrib.frontend_cache.backends.CloudflareBackend',
        'EMAIL': os.getenv('WAGTAIL_CF_EMAIL'),
        'TOKEN': os.getenv('WAGTAIL_CF_TOKEN'),
        'ZONEID': os.getenv('WAGTAIL_CF_ZONEID'),
    },
}

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = 'https://www.nerdventure.com'

ALLOWED_HOSTS = ['www.nerdventure.net', 'nerdventure.net'] 

# STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
# STATICFILES_STORAGE = 'CodeBlog.storage.GZIPStorage'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
COMPRESS_STORAGE = 'compressor.storage.BrotliCompressorFileStorage'

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# keep db connection open longer to increase performance when multiple db calls are needed
CONN_MAX_AGE = 30 # seconds

# MYSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4' # emoji
        },
    }
}

# wagtail-robots
ROBOTS_USE_SITEMAP = False
ROBOTS_SITEMAP_URLS = [
    'https://nerdventure.net/sitemap.xml',
]

COMPRESS_ENABLED = True
# COMPRESS_OFFLINE  = False

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'https://znmoore.com',
    'http://znmoore.com',
    'http://www.znmoore.com',
    'https://www.znmoore.com',
    'https://connect.facebook.net',
    'https://facebook.net',
    'https://facebook.com',
)

CORS_ALLOW_HEADERS = [
    'accept',
    'accepts',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = 'https://www.nerdventure.net'