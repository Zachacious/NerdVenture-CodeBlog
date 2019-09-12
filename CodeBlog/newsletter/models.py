from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, FieldRowPanel

from django.utils.translation import gettext_lazy as _
import datetime
from datetime import date
from django.utils import timezone

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

class Subscriber(models.Model):
    email = models.CharField(_("Email"), max_length=255, unique=True)
    date = models.DateTimeField(verbose_name="Subscribed On", default=timezone.now)
    optin_used = models.CharField(_("Optin Used"), max_length=255)
    subscribed = models.BooleanField(_("Subscribed"), default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    readonly_fields = ('date','optin_used',)
    
    panels = [
        FieldPanel('email'),
        FieldPanel('subscribed'),
        FieldRowPanel([
            FieldPanel('date'),
            FieldPanel('optin_used'),
        ]),
    ]     
    
    # def save(self, *args, **kwargs):

    #     # if a new instance - send welcome mail
    #     if self.subscribed:
    #         Object is a new instance
    #         context = {
                
    #         }
            
    #         msg_plain = render_to_string('newsletter/new_subscriber_email.txt', context)
    #         msg_html = render_to_string('newsletter/new_subscriber_email.html', context)

    #         send_mail(
    #             'Welcome Subscriber',
    #             msg_plain,
    #             settings.NEWSLETTER_FROM_EMAIL,
    #             [self.email],
    #             html_message=msg_html,
    #         )

    #     return super(Subscriber, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.email