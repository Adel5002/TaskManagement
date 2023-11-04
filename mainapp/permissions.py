from django.http import Http404
from .models import Project, ProjectGroup


class UserInGroupPermissionMixin:
    def has_permission(self):

        group = ProjectGroup.objects.filter(project__slug=self.kwargs.get('slug'))  # Getting Project Group

        # User takes perms if user have perms and the user is in the project group or user is author of the project
        return (self.request.user.has_perms(
            [
                'mainapp.add_task',
                'mainapp.change_task',
                'mainapp.delete_task',
            ]
        ) and self.request.user.groups.filter(name=self.request.user.groups.filter(pk__in=group.values('pk')).first())
          or Project.objects.filter(user=self.request.user))

    # Returning 404 error if user not in project group or not the author of group
    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            raise Http404
        return super().dispatch(request, *args, **kwargs)
