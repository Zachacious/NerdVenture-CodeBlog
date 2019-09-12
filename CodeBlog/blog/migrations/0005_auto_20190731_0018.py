# Generated by Django 2.2.3 on 2019-07-31 05:18

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('sidebar', '0001_initial'),
        ('blog', '0004_auto_20190730_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpostpage',
            name='sidebar',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='sidebar.Sidebar'),
        ),
        migrations.AlterField(
            model_name='blogpostpage',
            name='body',
            field=wagtail.core.fields.StreamField([('Heading', wagtail.core.blocks.CharBlock(classname='full title')), ('Rich_Text', wagtail.core.blocks.RichTextBlock()), ('Text', wagtail.core.blocks.TextBlock()), ('Image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('Embedded_Video', wagtail.embeds.blocks.EmbedBlock(icon='media')), ('HTML', wagtail.core.blocks.RawHTMLBlock()), ('Quote', wagtail.core.blocks.BlockQuoteBlock()), ('Email', wagtail.core.blocks.EmailBlock()), ('Optin', wagtail.snippets.blocks.SnippetChooserBlock('optin.Optin'))], blank=True, null=True),
        ),
    ]