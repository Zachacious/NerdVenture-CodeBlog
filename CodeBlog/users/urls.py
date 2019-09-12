from django.contrib import admin
from django.urls import include, path, re_path
from rest_auth.registration.views import VerifyEmailView, RegisterView
from allauth.account.views import confirm_email
from django.views.generic import TemplateView
from .views import ConfirmEmailView, PasswordResetConfirmation
from django.views.generic import TemplateView
# from rest_auth import views as rest_auth_views
# from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import password_reset_confirm
# from allauth.account.views import confirm_email as allauthemailconfirmation

urlpatterns = [
    path('api/v1/', include('rest_auth.urls')),
    path('api/v1/signup/', include('rest_auth.registration.urls')),
    # path('accounts/', include('allauth.urls')),
    re_path(r'^api/v1/account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(),
        name='account_confirm_email'),
    re_path(r'^api/v1/account-confirm-email/', VerifyEmailView.as_view(),
        name='account_email_verification_sent'),
    re_path(r'^api/v1/password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            PasswordResetConfirmation.as_view(),
            name='password_reset_confirm')
    # path('api/v1/password/', include('django.contrib.auth.urls')),
   
]

