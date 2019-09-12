# Generated by Django 2.2.3 on 2019-08-01 01:40

from django.db import migrations
import optin.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('optin', '0002_auto_20190731_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='optin',
            name='body',
            field=wagtail.core.fields.StreamField([('Heading', wagtail.core.blocks.CharBlock(classname='full title')), ('Rich_Text', wagtail.core.blocks.RichTextBlock()), ('Text', wagtail.core.blocks.TextBlock()), ('Image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('Embedded_Video', wagtail.embeds.blocks.EmbedBlock(icon='media')), ('HTML', wagtail.core.blocks.RawHTMLBlock()), ('Quote', wagtail.core.blocks.BlockQuoteBlock()), ('Email_Optin_Form', optin.blocks.EmailOptinFormBlock())]),
        ),
    ]
