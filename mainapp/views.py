from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.models import User, Permission
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import Project, Comment, ProjectGroup, Task
from .forms import AddCommentForm, CreteProjectForm, CreateNewGroupForm, CreateTaskForm
from .permissions import UserInGroupPermissionMixin


# PROJECT RENDERING SECTION
class ProjectsListView(LoginRequiredMixin, ListView):
    template_name = 'mainapp/index/index.html'
    model = Project
    context_object_name = 'projects'
    login_url = 'authentication:login'


class UserProjectListView(ListView):
    template_name = 'mainapp/index/user_project.html'
    model = User
    context_object_name = 'projects'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('slug'))
        projects = user.project_set.all()
        return projects


class UserProjectDetailView(DetailView):
    model = Project
    template_name = 'mainapp/project_details/project_details.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['group_details'] = ProjectGroup.objects.filter(project__slug=self.kwargs.get('slug'))
        context['comment_form'] = AddCommentForm
        return context


# PROJECT MANIPULATIONS SECTION
class CreateProject(CreateView):
    model = Project
    form_class = CreteProjectForm
    template_name = 'mainapp/project_manipulations/create_project.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('mainapp:proj_details', kwargs={'slug': self.object.slug})


class UpdateProject(UpdateView):
    model = Project
    form_class = CreteProjectForm
    template_name = 'mainapp/project_manipulations/update_project.html'

    def get_success_url(self):
        return reverse('mainapp:proj_details', kwargs={'slug': self.object.slug})


class DeleteProject(DeleteView):
    model = Project
    template_name = 'mainapp/index/user_project.html'

    def get_success_url(self):
        return reverse('mainapp:user_proj', kwargs={'slug': self.request.user})


# COMMENT SECTION
class AddComment(CreateView):
    model = Comment
    template_name = 'mainapp/project_details/project_details.html'
    form_class = AddCommentForm

    def form_valid(self, form):
        form.instance.project = Project.objects.get(slug=self.kwargs['slug'])
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('mainapp:proj_details', kwargs={'slug': self.object.project.slug})


class DeleteComment(DeleteView):
    model = Comment
    template_name = 'mainapp/project_details/project_details.html'

    def get_success_url(self):
        return reverse('mainapp:proj_details', kwargs={'slug': self.object.project.slug})


# GROUP SECTION

class GroupListView(ListView):
    model = ProjectGroup
    template_name = 'mainapp/group_manipulations/groups.html'
    context_object_name = 'groups'

    def get_queryset(self):
        return ProjectGroup.objects.filter(project__slug=self.kwargs.get('slug'))


class CreateGroup(CreateView):
    model = ProjectGroup
    template_name = 'mainapp/group_manipulations/create_group.html'
    form_class = CreateNewGroupForm
    success_url = '/'

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields['project'].queryset = self.request.user.project_set.all()
        return form

    def form_valid(self, form):
        form.instance.group_author = self.request.user
        instance = form.save()
        instance.permissions.set([33, 34, 35])  # id of permissions: add_task, change_task, delete_task
        instance.save()
        return super().form_valid(form)


class EditGroup(UpdateView):
    model = ProjectGroup
    template_name = 'mainapp/group_manipulations/edit_group.html'
    form_class = CreateNewGroupForm

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields['project'].queryset = self.request.user.project_set.all()
        return form

    def get_success_url(self):
        return reverse('mainapp:groups_list', kwargs={'slug': self.object.project.slug})


class DeleteGroup(DeleteView):
    model = ProjectGroup
    template_name = 'mainapp/group_manipulations/groups.html'

    def get_success_url(self):
        return reverse('mainapp:groups_list', kwargs={'slug': self.object.project.slug})


# TASK SECTION
class CreateTask(UserInGroupPermissionMixin, CreateView):
    model = Task
    template_name = 'mainapp/task_manipulations/create_task.html'
    form_class = CreateTaskForm

    def form_valid(self, form):
        form.instance.project = Project.objects.get(slug=self.kwargs['slug'])
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('mainapp:proj_details', kwargs={'slug': self.object.project.slug})


class EditTask(UpdateView):
    model = Task
    template_name = 'mainapp/task_manipulations/edit_task.html'
    form_class = CreateTaskForm

    def get_success_url(self):
        return reverse('mainapp:proj_details', kwargs={'slug': self.object.project.slug})


class DeleteTask(DeleteView):
    model = Task
    template_name = 'mainapp/project_details/project_details.html'

    def get_success_url(self):
        return reverse('mainapp:proj_details', kwargs={'slug': self.object.project.slug})
