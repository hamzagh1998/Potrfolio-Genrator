from django import forms
from .models import UserJob


class JobForm(forms.ModelForm):

    class Meta:

        model = UserJob
        fields = ['title', 'image', 'body', 'url']

class JobUpdateForm(forms.ModelForm):

    class Meta:

        model = UserJob
        fields = ['title', 'image', 'body', 'url']
