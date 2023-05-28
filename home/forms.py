from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import fields

class Register_Forms(UserCreationForm):
    password2 = forms.CharField(label="Retype Password ", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email': 'Email:'}

class Edit_Profile(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login', 'is_active']
        labels = {'email': 'Email'}

class Edit_AdminProfile(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = '__all__'
        labels = {'email': 'Email'}