from django.core.management.base import BaseCommand
from Users.models import User
from UsersSettings.models import UserSettings

class Command(BaseCommand):
    help = 'Create UserSettings for users that do not have them.'

    def handle(self, *args, **kwargs):
        users_without_settings = User.objects.filter(settings__isnull=True)
        for user in users_without_settings:
            UserSettings.objects.create(user=user)
            self.stdout.write(self.style.SUCCESS(f'Created UserSettings for {user.username}'))
