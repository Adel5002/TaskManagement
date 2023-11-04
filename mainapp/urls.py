from django.urls import path, include
from .views import (ProjectsListView, UserProjectListView, UserProjectDetailView, AddComment, DeleteComment,
                    CreateProject, UpdateProject, DeleteProject, CreateGroup, CreateTask, EditTask, DeleteTask,
                    EditGroup, DeleteGroup, GroupListView)

app_name = 'mainapp'

urlpatterns = [
    path("select2/", include("django_select2.urls")),

    # PROJECT SECTION
    path('', ProjectsListView.as_view(), name='main'),
    path('<slug:slug>', UserProjectListView.as_view(), name='user_proj'),
    path('create-project/', CreateProject.as_view(), name='new_project'),
    path('update-project/<slug:slug>/', UpdateProject.as_view(), name='update_project'),
    path('delete-project/<slug:slug>/', DeleteProject.as_view(), name='delete_project'),
    path('project/<slug:slug>/', UserProjectDetailView.as_view(), name='proj_details'),

    # COMMENT SECTION
    path('project/<slug:slug>/add-comment/', AddComment.as_view(), name='add_comment'),
    path('delete-comment/<int:pk>/', DeleteComment.as_view(), name='delete_comment'),

    # GROUP SECTION
    path('<slug:slug>/project-groups/', GroupListView.as_view(), name='groups_list'),
    path('create-group/', CreateGroup.as_view(), name='create_group'),
    path('edit-group/<int:pk>/', EditGroup.as_view(), name='edit_group'),
    path('delete-group/<int:pk>/', DeleteGroup.as_view(), name='delete_group'),

    # TASK SECTION
    path('project/<slug:slug>/create-task/', CreateTask.as_view(), name='create_task'),
    path('project/<slug:slug>/edit-task/<int:pk>/', EditTask.as_view(), name='edit_task'),
    path('project/<slug:slug>/delete-task/<int:pk>/', DeleteTask.as_view(), name='delete_task'),
]