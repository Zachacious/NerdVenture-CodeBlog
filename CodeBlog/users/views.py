from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import status
from django.http import HttpResponseRedirect

from django.contrib.auth import get_user_model

from django.contrib.auth.tokens import default_token_generator
from django.utils.http import is_safe_url, urlsafe_base64_decode
from django.core.exceptions import ValidationError
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.debug import sensitive_post_parameters

UserModel = get_user_model()

class ConfirmEmailView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request, *args, **kwargs):
        try:
            
            key = self.kwargs['key']
            return HttpResponseRedirect(
                settings.FRONTEND_EMAIL_CONFIRM_ENDPOINT + key)
            
        except:
            return Response('Invalid request data', status=status.HTTP_400_BAD_REQUEST)
        
class PasswordResetConfirmation(APIView):
    
    token_generator = default_token_generator
    
    @method_decorator(sensitive_post_parameters())
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        assert 'uidb64' in kwargs and 'token' in kwargs
        
        self.user = self.get_user(kwargs['uidb64'])
        
        if self.user is not None:
            uid = kwargs['uidb64']
            token = kwargs['token']
            if self.token_generator.check_token(self.user, token):
                return HttpResponseRedirect(
                    settings.FRONTEND_PASSWORD_RESET_CONFIRM_ENDPOINT 
                    + uid
                    + '/'
                    + token
                )
                
        return HttpResponseRedirect(
                    settings.FRONTEND_PASSWORD_RESET_CONFIRM_ENDPOINT + 'Failure'
                )
        
    def get_user(self, uidb64):
        try:
            # urlsafe_base64_decode() decodes to bytestring
            uid = urlsafe_base64_decode(uidb64).decode()
            user = UserModel._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist, ValidationError):
            user = None
        return user