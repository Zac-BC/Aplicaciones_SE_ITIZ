from rest_framework import viewsets

from .serializers import PokemonSerializer, SensoresSerializer
from .models import Pokemon, Sensores

class PokemonViewset (viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer


class SensoresViewset (viewsets.ModelViewSet):
    queryset = Sensores.objects.all()
    serializer_class = SensoresSerializer