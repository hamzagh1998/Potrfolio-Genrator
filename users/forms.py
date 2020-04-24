from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

class RegisterationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password']

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not authenticate(username=email, password=password):
                raise forms.ValidationError("Invalid input, Check the username or password!")

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['profile_pic', 'resume', 'blog', 'job', 'school', 'country', 'phone_num', 'body']

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
