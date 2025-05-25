from django.db import models

from Users.models import User
from django.apps import apps

class UserSettings(models.Model):
    user = models.OneToOneField('Users.User', on_delete=models.CASCADE, related_name='settings')
    private_account = models.BooleanField(default=False, blank=False)

    def __str__(self):
        return f"Settings of {self.user}"
