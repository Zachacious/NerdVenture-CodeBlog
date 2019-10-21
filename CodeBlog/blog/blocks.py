from wagtail.images import blocks as imageBlocks
from wagtail.core import blocks
from wagtail.embeds.blocks import EmbedBlock
from optin.blocks import OptinChooserBlock
from wagtailcodeblock.blocks import CodeBlock
from django.utils.translation import gettext_lazy as _
from django.db import models

class ImageChooserBlock(imageBlocks.ImageChooserBlock):
    class Meta:
        icon = 'image'
        label = 'Image(depricated)'
        template = 'blog/blocks/image_chooser_block.html'    
        
class AlignedImageBlock(blocks.StructBlock):
    image = imageBlocks.ImageChooserBlock()
    alignment = blocks.ChoiceBlock(choices=[
        ('center', 'Center'),
        ('right', 'Right'),
        ('left', 'Left'),
    ], default='center')
    
    class Meta:
        icon = 'image'
        label = 'Image(aligned)'
        template = 'blog/blocks/aligned_image_block.html' 

class BlogPostListBlock(blocks.StructBlock):
    title = blocks.CharBlock(blank=True, required=False)
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
        
        
class BootstrapCol(blocks.StructBlock):
    width = blocks.IntegerBlock(max_value=12, min_value=0, help_text='0 = auto', default=0)
    alignment = blocks.ChoiceBlock(choices=[
        ('center', 'Center'),
        ('right', 'Right'),
        ('left', 'Left'),
    ], default='center')
    vertical_center = blocks.BooleanBlock(default=False, blank=True, required=False)
    body = blocks.StreamBlock([
        (_('Rich_Text'), blocks.RichTextBlock()),
        (_('Text'), blocks.TextBlock()),
        (_('Image'), ImageChooserBlock(icon="image")),
        (_('Embedded_Video'), EmbedBlock(icon="media")),
        (_('HTML'), blocks.RawHTMLBlock()),
        (_('Quote'), blocks.BlockQuoteBlock()),
        (_('Optin'), OptinChooserBlock('optin.Optin')),
        (_('Code'), CodeBlock(label='Code Editor')),
        (_('Aligned_Image'), AlignedImageBlock()),
    ], blank=True, null=True, required=False)
    
    class Meta:
        icon = 'grip'
        label = 'Bootstrap Col'
        template = 'blog/blocks/bootstrap_Col.html'
        
class BootstrapRow(blocks.StructBlock):
    mobile_width = blocks.IntegerBlock(max_value=100, min_value=0, default=100)
    body = blocks.StreamBlock([
        (_('BootstrapCol'), BootstrapCol()),
    ], blank=True, null=True, required=False)
    
    class Meta:
        icon = 'placeholder'
        label = 'Bootstrap Row'
        template = 'blog/blocks/bootstrap_Row.html'
        
class ParallaxHeaderBlock(blocks.StructBlock):
    background = ImageChooserBlock(blank=True)
    title = blocks.CharBlock(blank=True)
    body = blocks.StreamBlock([
        (_('Rich_Text'), blocks.RichTextBlock()),
        (_('Text'), blocks.TextBlock()),
        (_('Image'), ImageChooserBlock(icon="image")),
        # (_('Image(aligned)'), AlignedImageBlock()),
        (_('Embedded_Video'), EmbedBlock(icon="media")),
        (_('HTML'), blocks.RawHTMLBlock()),
        (_('Quote'), blocks.BlockQuoteBlock()),
        (_('Optin'), OptinChooserBlock('optin.Optin')),
        (_('Code'), CodeBlock(label='Code Editor')),
        (_('Bootstrap_Row'), BootstrapRow()),
        (_('Bootstrap_Col'), BootstrapCol()),
        (_('Aligned_Image'), AlignedImageBlock()),
    ], blank=True, null=True, required=False)
    
    class Meta:
        icon = 'form'
        label = 'Parallax Header'
        template = 'blog/blocks/parallax_header.html'