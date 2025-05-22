
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from apps.users.models import Profile, User


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):

    if created:
        Profile.objects.create(user=instance)


@receiver(pre_save, sender=User)
def format_user_data(sender, instance, **kwargs):
    if instance.email:
        instance.email = instance.email.lower()
    if instance.username:
        instance.username = instance.username.capitalize()
