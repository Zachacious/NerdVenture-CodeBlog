# Generated by Django 2.2.5 on 2019-10-19 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('optin', '0021_auto_20191019_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='optin',
            name='blue_background',
            field=models.BooleanField(blank=True, default=False, verbose_name='Blue_background'),
        ),
    ]