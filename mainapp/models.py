from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (1, 'Started'),
    (2, 'In process'),
    (3, 'Finished'),
)


class Project(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    started = models.DateTimeField(auto_now_add=True)
    ended = models.DateTimeField(blank=True, null=True)


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField()
    status = models.CharField(choices=STATUS, max_length=120)
    deadline = models.DateField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

