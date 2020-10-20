from django.db import models

class Mapa(models.Model):
    nome = models.CharField(max_length = 30)

    def __str__(self):
        return self.nome

class Rota(models.Model):
    origem = models.CharField(max_length = 30)
    destino = models.CharField(max_length = 30)
    distancia = models.CharField(max_length = 30)
    
    def __str__(self):
        return self.origem