# Generated by Django 2.2.7 on 2020-04-21 21:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_remove_userjob_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='userjob',
            name='creation_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
