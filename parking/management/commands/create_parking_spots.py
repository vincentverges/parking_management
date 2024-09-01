import random
from django.core.management.base import BaseCommand
from parking.models import ParkingSpot

class Command(BaseCommand):
    help = 'Create a specified number of parking spots with random occupancy status'

    def add_arguments(self, parser):
        parser.add_argument('number_of_spots', type=int, help='Number of parking spots to create')

    def handle(self, *args, **kwargs):
        number_of_spots = kwargs['number_of_spots']
        for i in range(1, number_of_spots + 1):
            is_occupied = random.choice([True, False])
            spot, created = ParkingSpot.objects.get_or_create(spot_number=i)
            if created:
                spot.is_occupied = is_occupied
                spot.save()
                self.stdout.write(self.style.SUCCESS(f'Parking spot {i} created with status {"occupied" if is_occupied else "free"}'))
            else:
                self.stdout.write(self.style.WARNING(f'Parking spot {i} already exists'))

        self.stdout.write(self.style.SUCCESS(f'Successfully created {number_of_spots} parking spots with random occupancy status.'))