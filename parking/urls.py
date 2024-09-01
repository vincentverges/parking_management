from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParkingSpotViewSet

router = DefaultRouter()
router.register(r'spot', ParkingSpotViewSet)

urlpatterns = [
    path('', include(router.urls)),
]