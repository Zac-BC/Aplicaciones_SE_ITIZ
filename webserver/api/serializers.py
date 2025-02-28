
from rest_framework.serializers import ModelSerializer

from  .models import Pokemon, Sensor

class PokemonSerializer(ModelSerializer):
    class Meta():
        model = Pokemon
        fields = '__all__'
        
class SensorSerializer(ModelSerializer):
    class Meta():
        model = Sensor
        fields = '__all__'