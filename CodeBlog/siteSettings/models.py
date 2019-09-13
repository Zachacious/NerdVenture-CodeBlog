from django.db import models

from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.admin.edit_handlers import PageChooserPanel
from wagtail.core.models import Page

@register_setting
class SiteSettings(BaseSetting):
    header = models.ForeignKey(
        'header.Header',
        null=True,
        blank=True
        on_delete=models.SET_NULL,
        related_name='+'
    )
    
    footer = models.ForeignKey(
        'footer.Footer',
        null=True,
        blank=True
        on_delete=models.SET_NULL,
        related_name='+'
    )
    
    search_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    
    author_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    
    topic_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    
    content_panels = Page.content_panels + [
        SnippetChooserPanel('header'),
        SnippetChooserPanel('footer'),
        PageChooserPanel('search_page'),
        PageChooserPanel('author_page'),
        PageChooserPanel('topic_page'),
    ]