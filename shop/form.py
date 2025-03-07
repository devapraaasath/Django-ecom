from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class customuserform(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter username'}))
    Email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your email'}))
    password1=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your password'}))
    password2=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter confirm password'}))
    class meta:
        Model=User
        fields=['username','Email','password1','password2']