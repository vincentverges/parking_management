from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import ParkingSpot, ParkingTicket

class ParkingSpotTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        for i in range(1, 6):
            ParkingSpot.objects.create(spot_number=i, is_occupied=False)

    def test_get_all_spots(self):
        """Test pour récupérer toutes les places de parking"""
        response = self.client.get('/api/spot/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)

    def test_create_ticket(self):
        """Test pour obtenir un ticket pour une place disponible"""
        response = self.client.post('/api/spot/create_ticket/')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        ticket = ParkingTicket.objects.get(id=response.data['ticket']['id'])
        self.assertTrue(ticket.spot.is_occupied)

    def test_release_spot(self):
        """Test pour libérer une place de parking"""
        spot = ParkingSpot.objects.get(spot_number=1)
        ticket = ParkingTicket.objects.create(spot=spot)
        response = self.client.post(f'/api/spot/{spot.id}/release/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        spot.refresh_from_db()
        self.assertFalse(spot.is_occupied)