from django.contrib import admin
from desafio.models import Mapa,Rota


class Mapas(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links = ('id','nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Mapa, Mapas)

class Rotas(admin.ModelAdmin):
    list_display = ('id','origem','destino','distancia')
    list_display_links = ('id','origem','destino')
    search_fields = ('id',)
    list_per_page = 20
admin.site.register(Rota, Rotas)

# Register your models here.
