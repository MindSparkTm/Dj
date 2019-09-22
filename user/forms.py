from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from allauth.account.forms import SignupForm


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name',
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, label='Last Name', help_text='Last Name',
                                widget=forms.TextInput(attrs={'placeholder': 'First Name'}))

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username','email')
