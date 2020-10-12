from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .models import Profile

def save_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, name=instance.username)
        instance.profile.save()
        print('profile created')

post_save.connect(save_profile, sender=User)
