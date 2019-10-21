from wagtail.core import blocks
from wagtail.images import blocks as imageBlocks
from wagtail.documents import blocks as docBlocks

from django.utils.translation import gettext_lazy as _

class DownloadableBlock(blocks.StructBlock):
    image = imageBlocks.ImageChooserBlock()
    title = blocks.RichTextBlock()
    document = docBlocks.DocumentChooserBlock()
    
    class Meta:
        icon = 'download'
        label = 'Downloadable Item'
        template = 'downloader/blocks/downloadable_block.html'
        
        
class DownloadDisplayBlock(blocks.StructBlock):
    items = blocks.StreamBlock([
        # (_('Image'), imageBlocks.ImageChooserBlock()),
        (_('Downloadable'), DownloadableBlock()),
    ], blank=True, null=True, required=False)
    
    class Meta:
        icon = 'download'
        label = 'Download Display'
        template = 'downloader/blocks/download_display_block.html'
        