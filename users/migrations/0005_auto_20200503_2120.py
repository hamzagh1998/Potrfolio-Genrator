# Generated by Django 2.2.12 on 2020-05-03 20:20

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200424_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='resume',
            field=models.FileField(blank=True, default='user_logo.png', null=True, upload_to=users.models.resumeUploadLocation),
        ),
    ]
