from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.shortcuts import render
from dijkstra import DijkstraSPF,Graph
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from desafio.models import Mapa,Rota
from desafio.serializer import MapaSerializer, RotaSerializer

class MapasViewSet(viewsets.ModelViewSet):
    queryset = Mapa.objects.all()
    serializer_class = MapaSerializer


class RotasViewSet(viewsets.ModelViewSet):
    queryset = Rota.objects.all()
    serializer_class = RotaSerializer

@api_view(['GET'])
def CalculoRota(request):

    parametros =  JSONParser().parse(request)
    codmap = parametros['mapa']
    rotas = Rota.objects.all()

    rotas = rotas.filter(mapa__nome__icontains=codmap)
 
    graph = Graph()
    for rota in rotas:
        graph.add_edge(rota.origem, rota.destino, rota.distancia) 

    dijkstra = DijkstraSPF(graph, parametros['origem'])
 
    caminho = dijkstra.get_path(parametros['destino'])
    gasto = dijkstra.get_distance(parametros['destino'])/parametros['autonomia']*parametros['valorLitro']

    return JsonResponse({'origem': parametros['origem'],'destino': parametros['destino'],'gasto': gasto,'rota': caminho}, status=status.HTTP_404_NOT_FOUND) 
         


