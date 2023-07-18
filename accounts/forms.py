from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm, TextInput,PasswordInput,EmailInput

from .models import Customer

class CreateUserForm(UserCreationForm):

    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={'placeholder': 'Password confirm'}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        widgets = {
            'username': TextInput(attrs={'placeholder': 'username'}),
            'email':EmailInput(attrs={'placeholder':'Email'}),

        }


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']


