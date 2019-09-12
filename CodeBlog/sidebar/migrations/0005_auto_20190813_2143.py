# Generated by Django 2.2.4 on 2019-08-14 02:43

from django.db import migrations
import optin.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('sidebar', '0004_auto_20190731_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sidebar',
            name='body',
            field=wagtail.core.fields.StreamField([('Rich_Text', wagtail.core.blocks.RichTextBlock()), ('Text', wagtail.core.blocks.TextBlock()), ('Image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('Embedded_Video', wagtail.embeds.blocks.EmbedBlock(icon='media')), ('HTML', wagtail.core.blocks.RawHTMLBlock()), ('Optin', optin.blocks.OptinChooserBlock('optin.Optin'))]),
        ),
    ]
