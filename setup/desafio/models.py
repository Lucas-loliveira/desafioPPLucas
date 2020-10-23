from django.db import models

class Mapa(models.Model):
    nome = models.CharField(max_length = 30, unique=True)

    def __str__(self):
        return self.nome

class Rota(models.Model):
    mapa = models.ForeignKey(Mapa, related_name='rotas', on_delete=models.CASCADE)
    origem = models.CharField(max_length = 30)
    destino = models.CharField(max_length = 30)
    distancia = models.PositiveIntegerField()


