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

@api_view(['GET','POST'])
def CalculoRota(request):
    parametros =  JSONParser().parse(request)

    
    if not checkRequestValido(parametros):
        return JsonResponse({'mensagem': 'Parametros invalidos'}, status=status.HTTP_400_BAD_REQUEST)
    
    #obter rotas
    rotas = Rota.objects.all()
    rotas = rotas.filter(mapa__nome__icontains= parametros['mapa'])
    
    #checar se os objetos existem no banco
    if not rotas.exists():
        return JsonResponse({'mensagem': 'Mapa nao encontrado'}, status=status.HTTP_404_NOT_FOUND)

    if not  rotas.filter(origem__icontains= parametros['origem']):
        return JsonResponse({'mensagem': 'Origem nao encontrada no mapa'}, status=status.HTTP_404_NOT_FOUND)
    
    if not  rotas.filter(destino__icontains= parametros['destino']):
        return JsonResponse({'mensagem': 'Destino nao encontrado no mapa'}, status=status.HTTP_404_NOT_FOUND)

    
    graph = Graph()
    for rota in rotas:
        graph.add_edge(rota.origem, rota.destino, rota.distancia) 

    dijkstra = DijkstraSPF(graph, parametros['origem'])
    caminho = dijkstra.get_path(parametros['destino'])

    gasto = dijkstra.get_distance(parametros['destino'])/parametros['autonomia']*parametros['valorLitro']

    return JsonResponse({'origem': parametros['origem'],'destino': parametros['destino'],'gasto': gasto,'rota': caminho}, status=status.HTTP_200_OK) 
         

def checkRequestValido(parametros):
    #checar parametros string
    if not (isinstance(parametros['mapa'], str) and  isinstance(parametros['origem'], str) and isinstance(parametros['destino'], str) and isinstance(parametros['origem'], str)):
        return False
    #checar parametros float
    if not  (isinstance(parametros['autonomia'], (int, float)) and  isinstance(parametros['valorLitro'], (int, float))):
        return False
    #checar parametros positivos
    if not  (parametros['autonomia'] > 0 and  parametros['valorLitro'] > 0) :
        return False

    return True





