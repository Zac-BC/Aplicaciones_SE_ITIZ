from rest_framework.serializers import ModelSerializer
from .models import Pokemon, Sensores

class PokemonSerializer(ModelSerializer):
    class Meta():
        model = Pokemon
        fields = "__all__"

class SensoresSerializer(ModelSerializer):
    class Meta():
        model = Sensores
        fields = "__all__"