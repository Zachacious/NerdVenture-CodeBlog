from django.db import models
from wagtail.core.models import Page
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
)

@register_setting(icon='user')
class SocialSettings(BaseSetting):
    fb_share = models.BooleanField('Facebook Share', default=True)
    twitter_share = models.BooleanField('Twitter Share', default=True)
    # google_share = models.BooleanField('Google Share', default=True)
    linkedin_share = models.BooleanField('LinkedIn Share', default=True)
    reddit_share = models.BooleanField('Reddit Share', default=True)
    email_share = models.BooleanField('Email Share', default=True)
    printit = models.BooleanField('Print It', default=True)
    pintrest_share = models.BooleanField('Pintrest Share(Images)', default=True)
    
    content_panels = Page.content_panels + [
        FieldRowPanel([
            FieldPanel('fb_share'),
            FieldPanel('twitter_share'),
            # FieldPanel('google_share'),
            FieldPanel('linkedin_share'),
            FieldPanel('reddit_share'),
            FieldPanel('email_share'),
            FieldPanel('printit'),
            FieldPanel('pintrest_share'),
        ])
    ]
    
    class Meta:
        verbose_name = 'Social Media Share Buttons'
