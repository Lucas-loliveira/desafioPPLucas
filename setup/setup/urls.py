
from django.contrib import admin
from django.urls import path, include
from desafio.views import MapasViewSet, RotasViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('mapas',MapasViewSet, basename = 'Mapas' )
router.register('rotas',RotasViewSet, basename = 'Rotas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

]
