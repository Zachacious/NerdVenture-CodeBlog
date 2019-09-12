from django.urls import path
from blog import views
from rest_framework.urlpatterns import format_suffix_patterns
from wagtailcache.cache import nocache_page

urlpatterns = [
    path('msg/send/', nocache_page(views.ContactSendView.as_view()), name='blog-contactSendView'),
]

urlpatterns = format_suffix_patterns(urlpatterns)