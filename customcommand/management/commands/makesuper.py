from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
import os


class Command(BaseCommand):
    help = 'Added superuser'

    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                os.environ["DEFAULT_SUPER_USERNAME"],
                os.environ["DEFAULT_SUPER_EMAIL"],
                os.environ["DEFAULT_SUPER_PASSWORD"]
            )
            self.stdout.write(self.style.SUCCESS('Admin user has created'))
        else:
            self.stdout.write(self.style.SUCCESS('Admin user already exists'))
