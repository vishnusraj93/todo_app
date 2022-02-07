from . models import Task
from django import forms


class Todo_Form(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'priority', 'date']