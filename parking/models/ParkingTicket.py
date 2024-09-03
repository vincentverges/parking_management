from django.db import models
from django.utils import timezone
from parking.models.ParkingSpot import ParkingSpot

class ParkingTicket(models.Model):
    spot = models.OneToOneField(ParkingSpot, on_delete=models.CASCADE)
    issued_at = models.DateTimeField(default=timezone.now)