from django.apps import AppConfig
#from django.contrib.auth.models import User
#from django.db.models.signals import post_save
#from users.signals import save_profile


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals


