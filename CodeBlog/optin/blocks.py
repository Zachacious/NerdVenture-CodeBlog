from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.core import blocks

class OptinChooserBlock(SnippetChooserBlock):
    class Meta:
        icon = 'mail'
        label = 'Optin'
        template = 'optin/blocks/optin_chooser_block.html'
        
class EmailOptinFormBlock(blocks.StaticBlock):
    class Meta:
        icon = 'mail'
        label = 'Optin Email Form'
        template = 'optin/blocks/email_optin_form_block.html'