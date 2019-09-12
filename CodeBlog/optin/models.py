from django.db import models

from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from blog.blocks import ImageChooserBlock
from blog.blocks import ImageChooserBlock
from wagtail.snippets.models import register_snippet
from wagtail.core import blocks
from wagtail.embeds.blocks import EmbedBlock

from django.utils.translation import gettext as _

# from .blocks import OptinChooserBlock
from .blocks import EmailOptinFormBlock

@register_snippet
class Optin(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    
    body = StreamField([
        (_('Rich_Text'), blocks.RichTextBlock()),
        (_('Text'), blocks.TextBlock()),
        (_('Image'), ImageChooserBlock(icon="image")),
        (_('Embedded_Video'), EmbedBlock(icon="media")),
        (_('HTML'), blocks.RawHTMLBlock()),
        (_('Email_Optin_Form'), EmailOptinFormBlock()),
    ])
    
    panels = [
        FieldPanel('name'),
        StreamFieldPanel('body'),
    ]
    
    def __str__(self):
        return self.name
    

