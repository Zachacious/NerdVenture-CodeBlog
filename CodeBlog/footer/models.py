from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from django.utils.translation import gettext as _

@register_snippet
class Footer(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    copyright_text = models.CharField(_("Copyright Text"), max_length=255)
    
    menu = models.ForeignKey(
            'menu.Menu',
            null=True,
            blank=True,
            on_delete=models.SET_NULL,
            related_name='+',
            # help_text='Should be close to 400px X 100px'
        )
    
    panels = [
        FieldPanel('name'),
        FieldPanel('copyright_text'),
        SnippetChooserPanel('menu'),
    ]
    
    def __str__(self):
        return self.name
