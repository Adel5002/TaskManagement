# Generated by Django 4.2.6 on 2023-10-29 09:19

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('mainapp', '0002_alter_comment_options_alter_project_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectGroup',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.group')),
                ('assistants', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('group_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_author', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.project')),
            ],
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
    ]
