from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from .forms import UserLoginForm, UserSignupForm


class UserLogin(LoginView):
    template_name = 'authentication/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('mainapp:main')


class UserSignup(CreateView):
    form_class = UserSignupForm
    template_name = 'authentication/registration.html'
    success_url = reverse_lazy('authentication:login')


class UserLogout(LogoutView):
    template_name = 'mainapp/base.html'

    def get_success_url(self):
        return reverse_lazy('authentication:login')





