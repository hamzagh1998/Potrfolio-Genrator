# Generated by Django 2.2.7 on 2020-04-21 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_delete_jobs'),
        ('jobs', '0002_jobs_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Jobs',
            new_name='UserJob',
        ),
    ]
