from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail

from newsletter.models import Subscriber

from django.conf import settings

# from wagtailcache.cache import nocache_page

# @nocache_page
class ContactSendView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request, format=None):
        # get the required data sent from the contact form
        data = request.data 
                    
        if data:
            existing = False
            
            try:
                # get object if exist
                existing = Subscriber.objects.get(email=data['email'])
            except Exception as e:
                print(e)
                
            if not existing:
                # attempt to create a subscriber
                try:
                    if data['subscribe']: # subscribe checkbox was checked
                        sub = Subscriber()
                        sub.email = data['email']
                        sub.subscribed = True;
                        sub.optin_used = 'contact form'
                        sub.save()
                    else: # subscribe checkbox not checked
                        sub = Subscriber()
                        sub.email = data['email']
                        sub.subscribed = False;
                        sub.optin_used = 'contact form'
                        sub.save()
                except Exception as e:
                    print('failed to creat subscriber from contact email')
                    print(e)
            
            # attempt to send email to admin
            try:
                send_mail(
                    'Message from the site --',
                    str(data['message']),
                    str(data['email']),
                    [settings.EMAIL_MESSAGES_RECEIVER],
                    fail_silently=False,
                )
                
            except Exception as e:
                print(e)
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            
        return Response(data, status=status.HTTP_200_OK)
        
