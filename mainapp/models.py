from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from unidecode import unidecode

STATUS = (
    (1, 'Started'),
    (2, 'In process'),
    (3, 'Finished'),
)


class Tag(models.Model):
    tag = models.CharField(max_length=120)


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    file = models.FileField(upload_to='files/', null=True, blank=True)
    started = models.DateTimeField(auto_now_add=True)
    ended = models.DateTimeField(blank=True, null=True)
    tags = models.ManyToManyField(Tag)

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.name))
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Priority(models.Model):
    priority_name = models.CharField(max_length=60)


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField()
    status = models.CharField(choices=STATUS, max_length=120)
    deadline = models.DateField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    priority = models.ForeignKey(Priority, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag)

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.title))
        super(Task, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
