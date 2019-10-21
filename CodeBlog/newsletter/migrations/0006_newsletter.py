# Generated by Django 2.2.5 on 2019-10-20 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0010_document_file_hash'),
        ('newsletter', '0005_subscriber_date_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('target_subs', models.BooleanField(blank=True, default=True, verbose_name='target_subs')),
                ('target_non_subs', models.BooleanField(blank=True, default=True, verbose_name='target_non_subs')),
                ('template', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document')),
            ],
        ),
    ]
