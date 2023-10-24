from django.urls import path
from .views import ProjectsListView, UserProjectListView, UserProjectDetailView

app_name = 'mainapp'

urlpatterns = [
    path('', ProjectsListView.as_view(), name='main'),
    path('<slug:slug>', UserProjectListView.as_view(), name='user_proj'),
    path('project/<slug:slug>', UserProjectDetailView.as_view(), name='proj_details'),
]