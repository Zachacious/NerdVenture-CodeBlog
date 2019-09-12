from django.urls import path
from newsletter import views
from rest_framework.urlpatterns import format_suffix_patterns
from wagtailcache.cache import nocache_page

urlpatterns = [
    path('subscriber/<int:pk>/', nocache_page(views.SubscriberDetailsView.as_view())),
    path('subscriber/add/', nocache_page(views.SubscriberCreateView.as_view()), name='newsletter-createSubscriberView'),
]

urlpatterns = format_suffix_patterns(urlpatterns)