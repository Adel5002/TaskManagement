from django.urls import path
from .views import (ProjectsListView, UserProjectListView, UserProjectDetailView, AddComment, DeleteComment,
                    CreateProject, UpdateProject, DeleteProject)

app_name = 'mainapp'

urlpatterns = [
    path('', ProjectsListView.as_view(), name='main'),
    path('<slug:slug>', UserProjectListView.as_view(), name='user_proj'),
    path('create-project/', CreateProject.as_view(), name='new_project'),
    path('update-project/<slug:slug>/', UpdateProject.as_view(), name='update_project'),
    path('delete-project/<slug:slug>/', DeleteProject.as_view(), name='delete_project'),
    path('project/<slug:slug>/', UserProjectDetailView.as_view(), name='proj_details'),
    path('project/<slug:slug>/add-comment/', AddComment.as_view(), name='add_comment'),
    path('delete-comment/<int:pk>/', DeleteComment.as_view(), name='delete_comment'),
]