from django.urls import path, re_path
from news import views
from rest_framework.urlpatterns import format_suffix_patterns
from wagtailcache.cache import nocache_page

urlpatterns = [
    path('news/get_feed_page/', nocache_page(views.get_feed_page.as_view()), name='news-get-feed-page'),
]

urlpatterns = format_suffix_patterns(urlpatterns)