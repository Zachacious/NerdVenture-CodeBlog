from wagtail.images.blocks import ImageChooserBlock
from wagtail.core import blocks
from wagtail.embeds.blocks import EmbedBlock
from optin.blocks import OptinChooserBlock
from wagtailcodeblock.blocks import CodeBlock
from django.utils.translation import gettext_lazy as _
from django.db import models

class ImageChooserBlock(ImageChooserBlock):
    class Meta:
        icon = 'image'
        label = 'Image'
        template = 'blog/blocks/image_chooser_block.html'
        
class ParallaxHeaderBlock(blocks.StructBlock):
    background = ImageChooserBlock(blank=True)
    title = blocks.CharBlock(blank=True)
    body = blocks.StreamBlock([
        (_('Rich_Text'), blocks.RichTextBlock()),
        (_('Text'), blocks.TextBlock()),
        (_('Image'), ImageChooserBlock(icon="image")),
        (_('Embedded_Video'), EmbedBlock(icon="media")),
        (_('HTML'), blocks.RawHTMLBlock()),
        (_('Quote'), blocks.BlockQuoteBlock()),
        (_('Optin'), OptinChooserBlock('optin.Optin')),
        (_('Code'), CodeBlock(label='Code Editor')),
    ], blank=True)
    
    class Meta:
        icon = 'form'
        label = 'Parallax Header'
        template = 'blog/blocks/parallax_header.html'
        

class BlogPostListBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    root_page = blocks.PageChooserBlock()
    numPost = blocks.IntegerBlock()
    numCols = blocks.IntegerBlock()
    has_pagination = blocks.BooleanBlock(blank=True, required=False, default=True)
    
    class Meta:
        icon = 'grip'
        label = 'Blog Post List'
        template = 'blog/blocks/blog_post_list.html'
        
class BlockQuote(blocks.StructBlock):
    quote = blocks.TextBlock()
    author = blocks.CharBlock()
    
    class Meta:
        icon = 'openquote'
        label = 'Quotation'
        template = 'blog/blocks/block_quote.html'
        