from django.db import models
from django.urls import reverse
from django.utils import timezone
from phone_field import PhoneField
from tinymce.models import HTMLField
from django.utils.text import slugify
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
import os


def photoUploadLocation(instance, filename):
    file_path = f"user/{instance.user.id}/{instance.user.username}-{filename}"

    return file_path

def resumeUploadLocation(instance, filename):
    file_path = f"user/{instance.user.id}/{instance.user.username}-{filename}"

    return file_path


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_pic = models.ImageField(default="user_logo.png", upload_to=photoUploadLocation)
    resume = models.FileField(default="", blank=True, null=True, upload_to=resumeUploadLocation)
    blog = models.URLField(blank=True, null=True)
    job = models.CharField(max_length=100, blank=True)
    school = models.CharField(max_length=100, blank=True)
    country = CountryField(blank=True)
    phone_num = PhoneField(blank=True, help_text='Contact phone number')
    body = HTMLField()
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

@receiver(post_delete, sender=Profile)
def delete_image(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `Profile` object is deleted.
    """
    if instance.profile_pic:
        if os.path.isfile(instance.profile_pic.path):
            os.remove(instance.profile_pic.path)

@receiver(pre_save, sender=Profile)
def auto_delete_image_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `Album` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = Profile.objects.get(pk=instance.pk).resume
    except Profile.DoesNotExist:
        return False

    new_file = instance.resume
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
##################################################################################################
@receiver(post_delete, sender=Profile)
def delete_file(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `Profile` object is deleted.
    """
    if instance.resume:
        if os.path.isfile(instance.resume.path):
            os.remove(instance.resume.path)

@receiver(pre_save, sender=Profile)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `Profile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = Profile.objects.get(pk=instance.pk).resume
    except Profile.DoesNotExist:
        return False

    new_file = instance.resume
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
