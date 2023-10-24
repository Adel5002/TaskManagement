from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Project, Tag
from django.contrib.auth.models import User

class ProjectsListView(ListView):
    template_name = 'mainapp/index/index.html'
    model = Project

    # Redirecting to login page if user is not logged
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('authentication:login')

        return render(request, self.template_name, {'projects': self.model.objects.all()})


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
