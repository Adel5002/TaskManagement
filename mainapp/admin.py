from django.contrib import admin
from .models import *


class ProjectAdmin(admin.ModelAdmin):
    search_fields = ('name', 'user')
    prepopulated_fields = {'slug': ('name',)}


class TaskAdmin(admin.ModelAdmin):
    search_fields = ('title', 'user')
    prepopulated_fields = {'slug': ('title',)}


class TagAdmin(admin.ModelAdmin):
    search_fields = ('tag',)


class CommentAdmin(admin.ModelAdmin):
    search_fields = ('user', 'project')


class ProjectGroupAdmin(admin.ModelAdmin):
    search_fields = ('group_author', 'project')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TagAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(ProjectGroup, ProjectGroupAdmin)