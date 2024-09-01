from django.db import models
from django.utils import timezone
from parking.models.ParkingSpot import ParkingSpot

class ParkingTicket(models.Model):
    spot = models.OneToOneField(ParkingSpot, on_delete=models.CASCADE)
    issued_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Ticket pour la place {self.spot.spot_number} émis à {self.issued_at}"