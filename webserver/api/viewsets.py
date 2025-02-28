from rest_framework import viewsets

from .serializers import PokemonSerializer, SensorSerializer
from .models import Pokemon, Sensor

class PokemonViewset (viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

class SensorViewset (viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer