from django.core.management.base import BaseCommand
from marsapp.models import Fruit

class Command(BaseCommand):
    help = 'Seeds the database with specified fruits and counts'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting to seed data...')

        fruit_data = {
            "수박": 1000,
            "딸기": 10000,
            "포도": 100000
        }

        for fruit_name, count in fruit_data.items():
            for _ in range(count):
                Fruit.objects.create(name=fruit_name)

        self.stdout.write(self.style.SUCCESS('Data seeded successfully!'))
