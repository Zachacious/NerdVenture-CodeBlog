# Generated by Django 2.2.4 on 2019-08-27 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_blogpostpage_topics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpostpage',
            name='summary',
            field=models.TextField(blank=True, max_length=200, verbose_name='Summary Text'),
        ),
    ]