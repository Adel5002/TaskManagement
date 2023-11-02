from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from unidecode import unidecode
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.contrib.auth.models import Group

STATUS = (
    ('Стартовал', 'Started'),
    ('В процессе', 'In process'),
    ('Завершен', 'Finished'),
)

PRIORITY = (
    ('Низкий', 'Low'),
    ('Средний', 'Medium'),
    ('Высокий', 'High'),
    ('Наивысший', 'Highest'),
)


class Tag(models.Model):
    tag = models.CharField(max_length=120)

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    name = models.CharField(max_length=120, verbose_name='Название')
    slug = models.SlugField(unique=True)
    description = RichTextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/', null=True, blank=True, verbose_name='Фото')
    file = models.FileField(upload_to='files/', null=True, blank=True, verbose_name='Файлы')
    started = models.DateTimeField(auto_now_add=True, verbose_name='Начало')
    ended = models.DateTimeField(blank=True, null=True, verbose_name='Закончился')
    deadline = models.DateField(verbose_name='Дедлайн до')
    tags = models.ManyToManyField(Tag, verbose_name='Теги')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.name))
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mainapp:proj_details', kwargs={'slug': self.slug})


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    title = models.CharField(max_length=120, verbose_name='Название')
    description = RichTextField(verbose_name='Описание')
    status = models.CharField(choices=STATUS, max_length=120, verbose_name='Статус')
    deadline = models.DateField(verbose_name='Дедлайн до')
    started = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект')
    priority = models.CharField(choices=PRIORITY, max_length=60, verbose_name='Приоритет')


    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.title))
        super(Task, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Пользователь')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект')
    text = RichTextField(verbose_name='Текст')
    dateCreation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.project} - {self.user}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class ProjectGroup(Group):
    group_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='group_author', verbose_name='Автор группы')
    assistants = models.ManyToManyField(User, verbose_name='Ассистенты', related_name='assistant')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект')

