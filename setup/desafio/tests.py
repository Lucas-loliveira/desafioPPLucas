from django.test import TestCase
import pytest
import json


#constantes
rotasMapaValid = [{"origem":"A", "destino":"B", "distancia": 10},{"origem":"B", "destino":"D", "distancia": 15},{"origem":"A", "destino":"C", "distancia": 20},{"origem":"C", "destino":"D", "distancia": 30},{"origem":"B", "destino":"E", "distancia": 50},{"origem":"D", "destino":"E", "distancia": 30},{"origem":"Y", "destino":"Z", "distancia": 30}]
rotasMapaInvalid =  [{"or2igem":"B", "destino":"D", "distancia": 15},{"origem":"B", "destino":"D", "distancia": 15}]
mapaValid = "mapa teste"
origemValid = "B"
destinoValid = "D"
autonomiaValid = 10
valorLitroValid = 3
mapaInvalid = "mapa errado"
origemTypeInvalid  = 333
destinoInvalid  = "destino errado"
autonomiaInvalid  = -10
valorLitroInvalid  = 0


@pytest.fixture
def api_client():
   from rest_framework.test import APIClient
   return APIClient()

@pytest.mark.django_db(transaction=True)
@pytest.mark.parametrize(
   'nome, rotas, status_code', [
       ("", "", 400),
       ("",rotasMapaValid , 400),
       (mapaValid,rotasMapaInvalid, 400),
       (mapaValid,rotasMapaValid, 201),
   ]
)
def test_mapa(
   nome, rotas, status_code, api_client
):
   url = '/mapas/'
   data = {
       'nome': nome,
       'rotas': rotas
   }
   response = api_client.post(url, content_type='application/json', data=json.dumps(data))
   assert response.status_code == status_code




@pytest.mark.django_db(transaction=True)
@pytest.mark.parametrize(
   'mapa, origem, destino, autonomia, valorLitro, status_code', [
       (mapaValid,origemValid ,destinoValid,autonomiaValid,valorLitroValid, 200),#valido
       (mapaValid,origemTypeInvalid ,destinoValid,autonomiaValid,valorLitroValid, 400),#tipo origem invalido
       (mapaValid,origemValid ,destinoValid,autonomiaInvalid,valorLitroValid, 400),#autonomia invalida
       (mapaValid,origemValid ,destinoValid,autonomiaValid,valorLitroInvalid, 400),#valorLitro invalido
       (mapaInvalid,origemValid ,destinoValid,autonomiaValid,valorLitroValid, 404),#mapa nao encontrado
       (mapaValid,origemValid ,destinoInvalid,autonomiaValid,valorLitroValid, 404),#destino nao encontrado no mapa selecionado
   ]
)
def test_calculo(
   mapa, origem, destino, autonomia, valorLitro, status_code, api_client
):
    #criando mapa valido para teste de rota
    url = '/mapas/'
    data = {
        'nome': mapaValid,
        'rotas': rotasMapaValid
    }
    response = api_client.post(url, content_type='application/json', data=json.dumps(data))

    #teste de rota
    url = '/calculoRota/'
    data = {
        'mapa': mapa,
        'origem': origem,
        'destino': destino,
        'autonomia': autonomia,
        'valorLitro': valorLitro

    }
    response = api_client.post(url, content_type='application/json', data=json.dumps(data))
    assert response.status_code == status_code