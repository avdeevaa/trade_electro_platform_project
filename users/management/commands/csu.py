from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email="adminovic@mail.com",
            country='Russia',
            city='Moscow',
            street='Beautiful long street',
            house_number='1',
            is_staff=True,
            is_active=True,
            is_superuser=True
        )

        user.set_password('12345adminovic')
        user.save()
