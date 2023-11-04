from django import forms
from tempus_dominus.widgets import DatePicker
from django.contrib.auth.models import Group
from django_select2.forms import Select2MultipleWidget

from .models import Comment, Project, ProjectGroup, Task


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
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'})
        }


class CreateNewGroupForm(forms.ModelForm):
    class Meta:
        model = ProjectGroup
        fields = ('name', 'assistants', 'project')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Выберите название группы'}),
            'assistants': Select2MultipleWidget(
                attrs={'style': 'width: 100%', 'data-placeholder': 'Выберите сотрудников'}),
            'project': forms.Select(attrs={'class': 'form-control'}),
        }

    def save(self):
        assistants = self.cleaned_data['assistants']
        user = super().save(commit=True)
        group_name = self.cleaned_data['name']
        author = ProjectGroup.objects.get(name=group_name)
        author.group_author.groups.add(
            Group.objects.get(name=group_name))  # Adding Project Author to the development group
        for assist in assistants:
            assist.groups.add(Group.objects.get(name=Group.objects.get(name=group_name)))

        return user


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'status', 'deadline', 'priority')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'deadline': DatePicker(),
            'priority': forms.Select(attrs={'class': 'form-control'}),
        }
