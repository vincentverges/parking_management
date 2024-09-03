from pickle import FALSE

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import ParkingSpot, ParkingTicket
from .serializers import ParkingSpotSerializer, ParkingTicketSerializer


class ParkingSpotViewSet(viewsets.ModelViewSet):
    # Feature 3 : Get all spot, free or not
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer

    # Feature 1 : Get a parking's ticket with spot number
    @action(detail=False, methods=['POST'])
    def create_ticket(self,request):
        available_spot = ParkingSpot.objects.filter(is_occupied=False).first()
        if not available_spot:
            return Response({"error": "Aucune place disponible"},status=status.HTTP_404_NOT_FOUND)

        available_spot.is_occupied = True
        available_spot.save()

        ticket = ParkingTicket.objects.create(spot=available_spot)
        return Response({"ticket": ParkingTicketSerializer(ticket).data}, status=status.HTTP_201_CREATED)

    # Feature 2 : Exit from the parking and get the spot free
    @action(detail=True, methods=['POST'])
    def release(self,request, pk=None):
        try:
            ticket = ParkingTicket.objects.get(spot__pk=pk)
            ticket.spot.is_occupied = False
            ticket.spot.save()
            ticket.delete()
            return Response({"message": "Place libérée avec succès"}, status=status.HTTP_200_OK)
        except ParkingTicket.DoesNotExist:
            return Response({"error":"Ticket non trouvée pour cette place"}, status=status.HTTP_404_NOT_FOUND)

