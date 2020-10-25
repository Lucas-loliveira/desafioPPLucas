
# Desafio Próxima Porta: Entrega de mercadorias
Autor: Lucas da Silva de Oliveira (lucasoliveira783@gmail.com, https://www.linkedin.com/in/lucas-sil-oliveira)

## Motivação

Esse é um software desenvolvido para o desafio "malha logística" da empresa próxima porta. O programa foi desenvolvido utilizando a linguagem python 3.8.3 juntamente com o framework Django 3.1.2. O framework foi escolhido pois foram encontradas ferramentas como django rest e a biblioteca dijkstra que ajudaram na solução do desafio.

O projeto foi o primeiro contado do autor com a linguagem python e o framework Django, se apresentando como uma experiência enriquecedora para sua formação técnica no desenvolvimento de aplicativos Web.

## Introdução

O software tem como objetivo encontrar o menor caminho e calcular o gasto de combustível em um trajeto. Para isso, foram criadas duas APIs. A Primeira, para realizar o cadastro, consulta e deleção dos mapas. A segunda API, para retornar o menor trajeto entre dois pontos do mapa e realizar o cálculo do gasto de combustível.

## API Mapa

### URL: mapas/

### Descrição: Cadastro de mapas

### Método: POST

### Body: 
          {
            "nome": <string>,
            "rotas": [
                        {"origem":<string>, "destino":<string>, "distancia": <int>},
                        {"origem":<string>, "destino":<string>, "distancia": <int>},
                        ...
                    ]
          }

### Retorno: 
            {
                "id": <int>,
                "nome": <string>,
                "rotas": [
                        {"origem":<string>, "destino":<string>, "distancia": <int>},
                        {"origem":<string>, "destino":<string>, "distancia": <int>},
                        ...
                        ]
            }
          
### URL: mapas/

### Descrição: Recuperar todos os mapas cadastrados 

### Método: GET

### Retorno: 
            [
                {
                "id": <int>,
                "nome": <string>,
                "rotas": [
                            {"origem":<string>, "destino":<string>, "distancia": <int>},
                            {"origem":<string>, "destino":<string>, "distancia": <int>},
                            ...
                            ]
                },
                ...
            ]
        
### URL: mapas/<id:int>/

### Descrição: Recuperar um mapa especifico baseado em seu id   

### Método: GET

### Retorno: 
            {
              "id": <int>,
              "nome": <string>,
              "rotas": [
                          {"origem":<string>, "destino":<string>, "distancia": <int>},
                          {"origem":<string>, "destino":<string>, "distancia": <int>},
                          ...
                        ]
            }
          
           
### URL: mapas/<id:int>/

### Descrição: Deletar um mapa especifico baseado em seu id

### Método: DELETE


## API Calculo rota

        
### URL: /calculoRota/

### Descrição: Calcular a menor rota e o gasto de combustível   

### Método: GET ou POST
obs: O método POST foi adicionado nessa API pois não foi possivel realizar os testes da API com o método GET

### Body: 
          {
              "mapa": <string>,
              "origem": <string>,
              "destino": <string>,
              "autonomia": <float ou int>,
              "valorLitro":<float ou int>
          }

### Retorno: 
            {
                "origem": <string>,
                "destino": <string>,
                "gasto": <float>,
                "rota": [
                    <string>,
                    <string>,
                    <string>,
                    ...
                ]
            }

## Testes Unitarios
 
### Arquivo de teste: 
desafio/tests.py

### Comando para executar os testes: 
```bash
pytest
```


## Referências 
 
Referências utilizadas para realizar o desafio

Curso Alura: API com Django 3: Django Rest Framework <br>
Django REST framework: https://www.django-rest-framework.org <br>
pytest: https://djangostars.com/blog/django-pytest-testing/ <br>
API: https://bezkoder.com/django-rest-api/ <br>
Dijkstra: https://pypi.org/project/dijkstra/ <br>

 
 
 
 
 
 
 
 
