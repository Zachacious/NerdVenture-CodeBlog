# Generated by Django 2.2.5 on 2019-10-17 00:52

import blog.blocks
from django.db import migrations
import optin.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('sidebar', '0007_auto_20191016_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sidebar',
            name='body',
            field=wagtail.core.fields.StreamField([('Rich_Text', wagtail.core.blocks.RichTextBlock()), ('Text', wagtail.core.blocks.TextBlock()), ('Image(depricated)', blog.blocks.ImageChooserBlock(icon='image')), ('Image', wagtail.core.blocks.StructBlock([('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('center', 'Center'), ('right', 'Right'), ('left', 'Left')])), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('Embedded_Video', wagtail.embeds.blocks.EmbedBlock(icon='media')), ('HTML', wagtail.core.blocks.RawHTMLBlock()), ('Optin', optin.blocks.OptinChooserBlock('optin.Optin'))]),
        ),
    ]
