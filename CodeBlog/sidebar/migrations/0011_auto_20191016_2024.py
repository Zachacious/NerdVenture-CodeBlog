# Generated by Django 2.2.5 on 2019-10-17 01:24

import blog.blocks
from django.db import migrations
import optin.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('sidebar', '0010_auto_20191016_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sidebar',
            name='body',
            field=wagtail.core.fields.StreamField([('Rich_Text', wagtail.core.blocks.RichTextBlock()), ('Text', wagtail.core.blocks.TextBlock()), ('Image', blog.blocks.ImageChooserBlock(icon='image')), ('Embedded_Video', wagtail.embeds.blocks.EmbedBlock(icon='media')), ('HTML', wagtail.core.blocks.RawHTMLBlock()), ('Optin', optin.blocks.OptinChooserBlock('optin.Optin'))]),
        ),
    ]
