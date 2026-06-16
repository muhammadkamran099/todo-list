
from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TasksForm(forms.ModelForm):
    """build a form using database relation"""
    class Meta:
        model = Task
        fields = ['title']
        
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
