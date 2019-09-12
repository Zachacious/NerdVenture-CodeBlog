# Generated by Django 2.2.4 on 2019-08-12 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='socialsettings',
            options={'verbose_name': 'Social Media Share Buttons'},
        ),
        migrations.AddField(
            model_name='socialsettings',
            name='reddit_share',
            field=models.BooleanField(default=True, verbose_name='Reddit Share'),
        ),
    ]
