from django.db import models

class ParkingSpot(models.Model):
    spot_number = models.IntegerField(unique=True)
    is_occupied = models.BooleanField(default=False)

    def __str__(self):
        return f"Place {self.spot_number} - {'Occupé' if self.is_occupied else 'Libre'}"