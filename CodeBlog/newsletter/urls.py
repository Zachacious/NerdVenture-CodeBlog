from django.urls import path, re_path
from newsletter import views
from rest_framework.urlpatterns import format_suffix_patterns
from wagtailcache.cache import nocache_page

urlpatterns = [
    path('subscriber/<int:pk>/', nocache_page(views.SubscriberDetailsView.as_view())),
    path('subscriber/add/', nocache_page(views.SubscriberCreateView.as_view()), name='newsletter-createSubscriberView'),
    path('send/', nocache_page(views.SendMassMail.as_view()), name='newsletter-send-mass-mail-view'),
    path('open/<int:newsletterpk>/', nocache_page(views.Email_open_tracking.as_view()), name='email-open-tracking'),
    re_path(r'^unsubscribe/(?P<sentto>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$', nocache_page(views.Unsubscribe.as_view()), name='unsubscribe'),
]

urlpatterns = format_suffix_patterns(urlpatterns)