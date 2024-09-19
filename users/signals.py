from django.db.models.signals import post_save
from django.conf import settings

from .models import Profile


def create_Profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(create_Profile, sender=settings.AUTH_USER_MODEL)