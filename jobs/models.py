from django.db import models
from django.urls import reverse
from users.models import Profile
from django.utils import timezone
from tinymce.models import HTMLField
from django.utils.text import slugify


def upload_location(instance, filename):
    file_path = f"user/{instance.profile_id.user.id}/{instance.title}-{filename}"
    return file_path

class UserJob(models.Model):

    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(default="job.png", upload_to=upload_location)
    title = models.CharField(max_length=55, blank=False, null=False)
    body = HTMLField(max_length=1000, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    creation_date = models.DateField(default=timezone.now)

    def summary(self):
        return self.body[:50]+"..."

    def __str__(self):

        return f"{self.title}"
