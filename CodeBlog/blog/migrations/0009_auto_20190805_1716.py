# Generated by Django 2.2.4 on 2019-08-05 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190805_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpostpage',
            name='summary',
            field=models.TextField(blank=True, verbose_name='Summary Text'),
        ),
    ]