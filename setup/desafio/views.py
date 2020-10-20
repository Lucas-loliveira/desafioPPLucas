from rest_framework import viewsets
from desafio.models import Mapa,Rota
from desafio.serializer import MapaSerializer, RotaSerializer

class MapasViewSet(viewsets.ModelViewSet):
    queryset = Mapa.objects.all()
    serializer_class = MapaSerializer


class RotasViewSet(viewsets.ModelViewSet):
    queryset = Rota.objects.all()
    serializer_class = RotaSerializer
