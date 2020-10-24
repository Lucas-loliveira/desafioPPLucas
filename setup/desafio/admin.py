from django.contrib import admin
from desafio.models import Mapa,Rota


class Mapas(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links = ('id','nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Mapa, Mapas)


# Register your models here.
