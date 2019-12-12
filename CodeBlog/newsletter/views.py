# from django.shortcuts import render

from rest_framework.permissions import BasePermission, IsAdminUser, AllowAny, SAFE_METHODS
from rest_framework import generics
from .CustomAnonRateThrottle import CustomAnonRateThrottle

from .serializers import SubscriberSerializer
from .models import Subscriber, Newsletter

from django.http import HttpResponse
from django.views import View
import json

from django.utils.html import strip_tags
from django.template import Context, Template
from django.core.mail import get_connection, EmailMultiAlternatives

import datetime
from django.utils import timezone

from PIL import Image


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
    
class SubscriberDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
    permission_classes = [IsAdminUser|ReadOnly]
    throttle_classes = [CustomAnonRateThrottle]


# Email link from newsletter to frontend 
# when user clicks the unsubscribe button get the
# email param from the url on the frontend and send a
# put or patch request with subscribed set to false
class SubscriberCreateView(generics.CreateAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
    permission_classes = [AllowAny]
    throttle_classes = [CustomAnonRateThrottle]

# Send newsletter email to subscribers
class SendMassMail(View):
    permission_classes = [AllowAny]
    
    def post(self, request):

        try:
            #data sent via ajax
            data = json.loads(request.body)

            # Newsletter id(pk)
            pk = data['pk']

            template = Template(data['template'])

            subject = data['subject']
            fromEmail = data['fromEmail']

            subs = []
            non_subs = []

            if data['targetSubs']:
                subs = Subscriber.get_subscriber_emails()

            if data['targetNonSubs']:
                non_subs = Subscriber.get_non_subscriber_emails()

            recipients = list(subs + non_subs)

            # open connection using params in the settings
            connection =  get_connection(
                username=None,
                password=None,
                fail_silently=False,
            )
            messages=[]

            # create a message for each recipient
            for recipient in recipients:
                context = Context({'request': request,
                               'newsletterpk': pk,
                               'email': recipient})
                html = template.render(context)
                text = strip_tags(html)
                message = EmailMultiAlternatives(subject, text, fromEmail, [recipient], reply_to=['no-reply@nerdventure.net'])
                message.attach_alternative(html, 'text/html')
                messages.append(message)
            
            connection.send_messages(messages)
        except Exception as e:
            print(e)
            print('Failed to send Newsletter')
            return HttpResponse(status=500)

        try:
            newsletter = Newsletter.objects.get(pk=pk)
            
            newsletter.opens_last = 0
            newsletter.open_rate_last = 0

            newsletter.emails_sent_last = len(recipients)
            newsletter.last_sent_date = timezone.make_aware(datetime.datetime.now())

            newsletter.save()
        except Exception as e:
            print(e)
            print('Newsletter sent but newsletter instance not updated with data')
            return HttpResponse(status=500)

        return HttpResponse(status=200)
    
class Email_open_tracking(View):
    
    # TODO - track which users have opened
    def get(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('newsletterpk')
            
            newsletter = Newsletter.objects.get(pk=pk)
            
            newsletter.opens_last = newsletter.opens_last + 1
            newsletter.open_rate_last = (newsletter.opens_last / newsletter.emails_sent_last) * 100
            
            newsletter.save()
        except Exception as e:
            print(e)
            print('Unable to save tracking data')
            return HttpResponse(status="500", content_type="image/png")
            
        red = Image.new('RGB', (1, 1))
        response = HttpResponse(content_type="image/png")
        red.save(response, "PNG")
        
        return response
    
class Unsubscribe(View):
    
    def get(self, request, *args, **kwargs):
        try:
            email = kwargs.get('sentto')
            
            sub = Subscriber.objects.get(email=email)
            
            sub.subscribed = False
            
            sub.save()
        except Exception as e:
            print(e)
            print('Unable to unsubscribe. Try again later.')
            return HttpResponse('''
                            <html>
                            <body style="background-color: #ededef; font-size: 1.25em;">
<header style="background-color: #094ecf; width: 100%; margin-bottom: 10px; margin-left: auto; margin-right: auto;">
<a href="https://www.nerdventure.net">
<img src="https://www.nerdventure.net/media/images/NerdVentureLogo4_AJ2yR0e.width-225.png" style="margin-bottom: 10px; margin-left: auto; margin-right: auto;" />
</a>
</header>
<h1 style="text-align: center;">Unable to unsubscribe. Please contact support@nerdventure.net.</h1>
</body>
                            </html>
                            ''', status=500)
        
        # repond with unsubscribed page
        return HttpResponse('''
                            <html>
                            <body style="background-color: #ededef; font-size: 1.25em;">
<header style="background-color: #094ecf; width: 100%; margin-bottom: 10px; margin-left: auto; margin-right: auto;">
<a href="https://www.nerdventure.net">
<img src="https://www.nerdventure.net/media/images/NerdVentureLogo4_AJ2yR0e.width-225.png" style="margin-bottom: 10px; margin-left: auto; margin-right: auto;" />
</a>
</header>
<h1 style="text-align: center;">You have been unsubscribed</h1>
</body>
                            </html>
                            ''', status=200)