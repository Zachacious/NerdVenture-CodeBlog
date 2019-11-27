from django.core.management.base import BaseCommand, CommandError
from feeds.models import Post
from django.template import Context, Template
from django.core.mail import get_connection, EmailMultiAlternatives
from newsletter.models import Subscriber
from django.utils.html import strip_tags
from django.core.files.storage import get_storage_class
from django.conf import settings

import datetime 
import calendar
import pytz 

class Command(BaseCommand):
    help = 'Create and send the weekly newsletter'
    
    def handle(self, *args, **options):
        
        tz = pytz.timezone('America/Chicago')
        date = datetime.datetime.now()
        local_date = tz.localize(date)
        weekday = calendar.day_name[local_date.weekday()]
        
        if not(weekday == 'tuesday'):
            print('Waiting on Tuesday')
            return
        
        storage_class = get_storage_class(settings.STATICFILES_STORAGE)
        
        template_url = 'email_templates/weekly_mail_template.html'
                        
        subs = Subscriber.get_subscriber_emails()

        recipients = list(subs)
        
        subject = 'The latest nerd news from around the web'
        
        from_email = 'WeeklyUpdate@nerdventure.net'

        # open connection using params in the settings
        connection =  get_connection(
            username=None,
            password=None,
            fail_silently=False,
        )
        messages=[]
        
        html_file = storage_class().open(template_url)
        template = Template((html_file.read()).decode("utf-8"))

        # create a message for each recipient
        for recipient in recipients:
            context = Context({
                            'email': recipient
                            })
            html = template.render(context)
            text = strip_tags(html)
            message = EmailMultiAlternatives(subject, text, from_email, [recipient], reply_to=['no-reply@nerdventure.net'])
            message.attach_alternative(html, 'text/html')
            messages.append(message)
        
        connection.send_messages(messages)
        
        