from django import forms
from tempus_dominus.widgets import DatePicker

from .models import Comment, Project


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

        widgets = {
            'text': forms.Textarea()
        }


class CreteProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'description', 'photo', 'file', 'deadline', 'tags')

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Имя проекта'}, ),
            'description': forms.Textarea(),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
            'deadline': DatePicker(),
            'tags': forms.SelectMultiple()
        }