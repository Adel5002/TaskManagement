from django.shortcuts import render, redirect
from django.views.generic import ListView


# def index(request):
#     if not request.user.is_authenticated:
#         return redirect('authentication:login')
#     return render(request, 'mainapp/index/index.html')


class MainView(ListView):
    template_name = 'mainapp/index/index.html'

    # Redirecting to login page if user is not logged
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('authentication:login')
        return render(request, 'mainapp/index/index.html')
