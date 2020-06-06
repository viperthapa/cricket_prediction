from django import forms
from .views import *
from django.contrib.auth.models import User
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Enter username'}))
    password = forms.CharField(
        max_length=20, widget=forms.PasswordInput(attrs={'placeholder': ' Enter password'}))


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=20, widget=forms.TextInput())
    password = forms.CharField(max_length=20, widget=forms.PasswordInput())
    confirm_password = forms.CharField(
        max_length=20, widget=forms.PasswordInput())
    

    class Meta:
        model = Player
        fields = ['username', 'password', 'confirm_password', 'name', 'address',
                  'mobile', 'image']

    def clean_confirm_password(self):

        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                'password and confirm_password did not match')
        return confirm_password

    def clean_username(self):
        username = self.cleaned_data.get('username')
        users = User.objects.filter(username=username)
        if users.exists():
            raise forms.ValidationError('username already exists')
        return username
