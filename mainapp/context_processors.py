from .models import Project,Tag

def projects(request):
    return {'projects': Project.objects.all()}

def tags(request):
    return {'tags': Tag.objects.all()}