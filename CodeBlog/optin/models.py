from django.db import models

from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from blog.blocks import ImageChooserBlock, AlignedImageBlock, BootstrapCol, BootstrapRow
from wagtail.snippets.models import register_snippet
from wagtail.core import blocks
from wagtail.embeds.blocks import EmbedBlock

from django.utils.translation import gettext as _

# from .blocks import OptinChooserBlock
from .blocks import EmailOptinFormBlock, EmailOptinCTABlock

@register_snippet
class Optin(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    blue_background = models.BooleanField(_("Blue_background"), blank=True, default=False)
    dont_hide_from_subcribers = models.BooleanField(_("Dont_Hide_From_Subscribers"), blank=True, default=False)
    
    body = StreamField([
        (_('Bootstrap_Row'), BootstrapRow()),
        (_('Bootstrap_Col'), BootstrapCol()),
        (_('Rich_Text'), blocks.RichTextBlock()),
        (_('Text'), blocks.TextBlock()),
        (_('Image'), ImageChooserBlock(icon="image")),
        # (_('Image(aligned)'), AlignedImageBlock()),
        (_('Embedded_Video'), EmbedBlock(icon="media")),
        (_('HTML'), blocks.RawHTMLBlock()),
        (_('Email_Optin_Form'), EmailOptinFormBlock()),
        (_('Aligned_Image'), AlignedImageBlock()),
        (_('Email_Optin_CTA_Form'), EmailOptinCTABlock()),
    ])
    
    panels = [
        FieldPanel('name'),
        FieldPanel('blue_background'),
        FieldPanel('dont_hide_from_subcribers'),
        StreamFieldPanel('body'),
    ]
    
    def __str__(self):
        return self.name
    