from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParkingSpotViewSet

router = DefaultRouter()
router.register(r'spot', ParkingSpotViewSet, basename='spot')

urlpatterns = [
    path('api/', include(router.urls)),
]