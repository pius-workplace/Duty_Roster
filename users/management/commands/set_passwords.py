from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Set default password for all users'

    def handle(self, *args, **options):
        users = User.objects.all()
        for user in users:
            user.set_password('password123')
            user.save()
            self.stdout.write(f'Set password for user: {user.username}')
        self.stdout.write(self.style.SUCCESS('Successfully set passwords for all users'))
