from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, FieldRowPanel

from django.utils.translation import gettext_lazy as _
import datetime
from datetime import date
from django.utils import timezone

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from wagtail.documents.models import Document
from wagtail.documents.edit_handlers import DocumentChooserPanel

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
    
    # Returns only the email fields from the subscribers in a list
    @classmethod
    def get_subscriber_emails(cls):
        return list(cls.objects.filter(subscribed=True).values_list('email', flat=True).distinct())

    # Returns only the email fields from the non-subscribers in a list
    @classmethod
    def get_non_subscriber_emails(cls):
        return list(cls.objects.filter(subscribed=False).values_list('email', flat=True).distinct())


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
    
class Newsletter(models.Model):
    title = models.CharField(_("title"), max_length=100)
    subject = models.CharField(_("subject"), max_length=255, default='The latest')
    fromEmail = models.EmailField(_("from_email"), default='Newsletter@NerdVenture.net')
    target_subs = models.BooleanField(_("target_subs"), default=True, blank=True)
    target_non_subs = models.BooleanField(_("target_non_subs"), default=True, blank=True)
    template = models.TextField(_("template"), default='<html></html>')
    emails_sent_last = models.IntegerField(_("number_sent"), default=0, blank=True, null=True, editable=False)
    open_rate_last = models.IntegerField(_("open_rate"), help_text="Percent", default=0, blank=True, null=True, editable=False)
    opens_last = models.IntegerField(_("opens_last"), help_text="total opens since last send", default=0, blank=True, null=True, editable=False)
    last_sent_date = models.DateTimeField(_("last_sent"), blank=True, null=True, editable=False)
    
    panels = [
        FieldPanel('title'),
        FieldPanel('subject'),
        FieldPanel('fromEmail'),
        FieldPanel('target_subs'),
        FieldPanel('target_non_subs'),
        FieldPanel('template'),
        # DocumentChooserPanel('template'),
    ]
    
    def __str__(self):
        return self.title