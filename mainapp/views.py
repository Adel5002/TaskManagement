from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Project, Comment
from .forms import AddCommentForm


class ProjectsListView(ListView):
    template_name = 'mainapp/index/index.html'
    model = Project

    # Redirecting to login page if user is not logged
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('authentication:login')

        context = {
            'projects': self.model.objects.all(),
        }
        return render(request, self.template_name, context)


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

        context['comment_form'] = AddCommentForm
        return context

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



