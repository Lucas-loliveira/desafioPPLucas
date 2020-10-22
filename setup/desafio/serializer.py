from rest_framework import serializers 
from desafio.models import Mapa, Rota


class RotaSerializer(serializers.ModelSerializer):
     class Meta:
        model = Rota
        fields =  ['origem',  'destino', 'distancia']


class MapaSerializer(serializers.ModelSerializer):
    rotas = RotaSerializer(many=True)
    class Meta:
        model = Mapa
        fields = ['nome',  'rotas']

    def create(self, validated_data):
        rotas_data = validated_data.pop('rotas')
        mapa = Mapa.objects.create(**validated_data)
        for rota_data in rotas_data:
            Rota.objects.create(mapa=mapa, **rota_data)
        return mapa

