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
from django.utils import timezone

class Command(BaseCommand):
    help = 'Create and send the weekly newsletter'
    
    def handle(self, *args, **options):
        # make sure it is a tuesday or pass until it is
        
        tz = pytz.timezone('America/Chicago')
        date = datetime.datetime.now()
        local_date = tz.localize(date)
        weekday = calendar.day_name[local_date.weekday()]
        
        if not(weekday == 'tuesday'):
            print('Waiting on Tuesday')
            return
        
        # remove the previous weeks post
        
        old_posts = Post.objects.filter(created__lt=timezone.now()-datetime.timedelta(days=7))
        for old_post in old_posts:
            old_post.delete()
            
        # get the email template
        
        storage_class = get_storage_class(settings.STATICFILES_STORAGE)
        
        template_url = 'email_templates/weekly_mail_template.html'
        
        # get list of subscriber email addresses
                        
        subs = Subscriber.get_subscriber_emails()

        recipients = list(subs) # TODO: remove
        
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
        
        
        