from django.db.models.signals import post_save, post_delete
from django.contrib.auth import get_user_model
User = get_user_model()

from .models import Profile


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(create_profile, sender=User)


