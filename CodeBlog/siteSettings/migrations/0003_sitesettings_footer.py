# Generated by Django 2.2.3 on 2019-07-30 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('footer', '0001_initial'),
        ('siteSettings', '0002_sitesettings_search_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='footer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='footer.Footer'),
        ),
    ]