from django.db import models
from django.urls import reverse
from django.utils import timezone
from phone_field import PhoneField
from django.utils.text import slugify
from django.contrib.auth.models import User
from django_countries.fields import CountryField


def photoUploadLocation(instance, filename):
    file_path = f"user/{instance.user.id}/{instance.user.username}-{filename}"

    return file_path

def resumeUploadLocation(instance, filename):
    file_path = f"user/{instance.user.id}/{instance.user.username}-{filename}"

    return file_path


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_pic = models.ImageField(default="user_logo.png", upload_to=photoUploadLocation)
    resume = models.FileField(blank=True, null=True, upload_to=resumeUploadLocation)
    blog = models.URLField(blank=True, null=True)
    job = models.CharField(max_length=100, blank=True)
    school = models.CharField(max_length=100, blank=True)
    country = CountryField(blank=True)
    phone_num = PhoneField(blank=True, help_text='Contact phone number')
    body = models.TextField(blank=True, max_length=2000)
    creation_date = models.DateField(default=timezone.now)
    slug = models.SlugField(unique=True)

    def summary(self):
        return self.body[:50]+'...'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.first_name)
        super(Profile, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('user_profile', kwargs={'slug': self.slug})

    def __str__(self):
        return f"{self.user.username} Profile"
