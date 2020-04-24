# Generated by Django 2.2.7 on 2020-04-21 15:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields
import phone_field.models
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(default='user_logo.png', upload_to=users.models.photoUploadLocation)),
                ('resume', models.FileField(blank=True, null=True, upload_to=users.models.resumeUploadLocation)),
                ('blog', models.URLField(blank=True, null=True)),
                ('job', models.CharField(blank=True, max_length=100)),
                ('school', models.CharField(blank=True, max_length=100)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('phone_num', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('body', models.TextField(blank=True, max_length=2000)),
                ('creation_date', models.DateField(default=django.utils.timezone.now)),
                ('slug', models.SlugField(unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
