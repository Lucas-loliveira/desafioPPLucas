from rest_framework import serializers 
from desafio.models import Mapa, Rota

class MapaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mapa
        fields = '__all__'

class RotaSerializer(serializers.ModelSerializer):
     class Meta:
        model = Rota
        fields = '__all__'
