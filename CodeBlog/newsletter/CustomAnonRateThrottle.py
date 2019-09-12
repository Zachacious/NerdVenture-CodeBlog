from django.core.cache import caches
from rest_framework.throttling import AnonRateThrottle

# To handle custom django cache for wagtail
class CustomAnonRateThrottle(AnonRateThrottle):
    pass
    # cache = caches['alternate']