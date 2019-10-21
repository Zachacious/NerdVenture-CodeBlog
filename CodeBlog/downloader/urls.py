from django.conf.urls import url

from .views import serve

urlpatterns = [
    url(r'^(\d+)/(.*)$', serve, name='wagtaildocs_serve'),
]