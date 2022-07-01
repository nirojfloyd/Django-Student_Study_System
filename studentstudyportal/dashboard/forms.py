from cgitb import text
from dataclasses import fields
from pyexpat import model
from django import forms
from . models import *
from django.contrib.auth.forms import UserCreationForm



class DashboardSearch(forms.Form):
    text = forms.CharField(max_length=100,label="Enter your text") 

#for user registeration
class UserRegistrationForm(UserCreationForm):
   class Meta:
    model = User
    fields = ['username','email','password1','password2']
