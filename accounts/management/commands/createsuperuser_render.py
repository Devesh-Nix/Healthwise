from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    help = "Create default superuser only on first deploy"

    def handle(self, *args, **kwargs):
        User = get_user_model()
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                username="admin",
                email="admin@example.com",
                password="Admin@1234"
            )
            self.stdout.write(self.style.SUCCESS("Superuser created successfully."))
            print(f"Users: {User.objects.all()}")
            print(User.objects.filter(is_superuser=True, is_staff=True))

            # 🔐 Delete this file after creation
            path_to_file = os.path.abspath(__file__)
            os.remove(path_to_file)
            self.stdout.write(self.style.WARNING(f"{path_to_file} has been deleted for security."))

        else:
            self.stdout.write(self.style.WARNING("Superuser already exists. No action taken."))
            # 🔐 Delete this file after creation
            