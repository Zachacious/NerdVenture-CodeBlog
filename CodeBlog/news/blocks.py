from wagtail.core import blocks

class NewsWallBlock(blocks.StaticBlock):
    
    class Meta:
        icon = 'image'
        label = 'News Wall'
        template = 'news/blocks/news_wall_block.html' 