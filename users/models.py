from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, unique=True)
    phone = models.CharField(max_length=11, null=True, unique=True)
    email = models.EmailField(null=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, default='profile1.png')
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
