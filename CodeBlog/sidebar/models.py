from django.db import models

from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
# from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.core import blocks
from wagtail.embeds.blocks import EmbedBlock

from django.utils.translation import gettext as _

from optin.blocks import OptinChooserBlock
from blog.blocks import ImageChooserBlock, AlignedImageBlock

@register_snippet
class Sidebar(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    fixed = models.BooleanField(_("Fixed Position"), default=False)
    body = StreamField([
        # (_('Heading'), blocks.CharBlock(classname="full title")),
        (_('Rich_Text'), blocks.RichTextBlock()),
        (_('Text'), blocks.TextBlock()),
        (_('Image'), ImageChooserBlock(icon="image")),
        # (_('Image(aligned)'), AlignedImageBlock()),
        (_('Embedded_Video'), EmbedBlock(icon="media")),
        (_('HTML'), blocks.RawHTMLBlock()),
        # (_('Quote'), blocks.BlockQuoteBlock()),
        # (_('Email_Form'), blocks.EmailBlock()),
        # (_('OptinForm'), OptinChooserBlock()),
        (_('Optin'), OptinChooserBlock('optin.Optin')),
        (_('Aligned_Image'), AlignedImageBlock()),
    ])
    
    panels = [
        FieldPanel('name'),
        FieldPanel('fixed'),
        StreamFieldPanel('body'),
    ]
    
    def __str__(self):
        return self.name
    
