from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from newsletter import urls as newsletter_urls
from blog import urls as blog_urls

from wagtail.contrib.sitemaps.views import sitemap

from wagtailcache.cache import nocache_page

from .api import api_router

urlpatterns = [
    

    url(r'^sitemap\.xml$', nocache_page(sitemap)),
    url(r'^newsletter/api/v1/', include(newsletter_urls)),
    url(r'^contact/api/v1/', include(blog_urls)),

    url(r'^jackalope/', admin.site.urls),

    url(r'^cms/jackalope/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    
    # url(r'^users/', include('users.urls')),
    
    url(r'^api/v1/wt/', api_router.urls),
    
    url(r'^robots\.txt', include('robots.urls')),


    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    url(r'', include(wagtail_urls)),

    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    url(r'^pages/', include(wagtail_urls)),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # urlpatterns += [
    #     re_path(r'^favicon\.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'myapp/images/favicon.ico'))
    # ]