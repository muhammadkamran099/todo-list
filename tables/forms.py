from django import forms
from .models import Task

class TasksForm(forms.ModelForm):
    """build a form using database relation"""
    class Meta:
        model = Task
        fields = ['title']