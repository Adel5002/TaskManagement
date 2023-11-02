# from django.dispatch import receiver
# from .models import ProjectGroup
# from django.db.models.signals import post_save, pre_save
# from django.contrib.auth.models import Group, User
#
#
# @receiver(post_save, sender=ProjectGroup)
# def save_assistants_in_group(sender, instance, created, **kwargs):
#     if created:
#         group = Group.objects.get(name=instance.name)
#         instance.group_author.groups.add(group)
#         instance.save()
#
#
