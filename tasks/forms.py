from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['content', 'deadline', 'tags']
        widgets = {
            'deadline': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                    'placeholder': 'YYYY-MM-DD HH:MM',
                    'class': 'form-control',
                }
            ),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
