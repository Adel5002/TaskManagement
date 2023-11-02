from django.http import Http404
from django.contrib.auth.models import Group
from .models import Project, ProjectGroup
from django.contrib.auth.mixins import PermissionRequiredMixin


class UserInGroupPermissionMixin:
    def has_permission(self):

        group = ProjectGroup.objects.filter(project__slug=self.kwargs.get('slug')).values('name')
        print(group[0]['name'])
        return self.request.user.has_perms(
            [
                'mainapp.add_task',
                'mainapp.change_task',
                'mainapp.delete_task',
            ]
        ) and self.request.user.groups.filter(name=group[0]['name'])

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            raise Http404
        return super().dispatch(request, *args, **kwargs)
