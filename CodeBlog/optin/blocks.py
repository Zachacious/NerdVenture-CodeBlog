from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.core import blocks
from wagtail.documents import blocks as docBlocks

class OptinChooserBlock(SnippetChooserBlock):
    class Meta:
        icon = 'mail'
        label = 'Optin'
        template = 'optin/blocks/optin_chooser_block.html'
        
class EmailOptinFormBlock(blocks.StaticBlock):    
    class Meta:
        icon = 'mail'
        label = 'Optin Email Form(depricated)'
        template = 'optin/blocks/email_optin_form_block.html'
        
class EmailOptinCTABlock(blocks.StructBlock):
    cta_text = blocks.TextBlock()
    cta_action_loadpage = blocks.PageChooserBlock(required=False)
    cta_action_download = docBlocks.DocumentChooserBlock(required=False)
    
    class Meta:
        icon = 'mail'
        label = 'Optin Email Form'
        template = 'optin/blocks/email_optin_form_block.html'