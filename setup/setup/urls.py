
from django.contrib import admin
from django.urls import path, include
from desafio.views import MapasViewSet, RotasViewSet, CalculoRota
from rest_framework import routers


router = routers.DefaultRouter()
router.register('mapas',MapasViewSet, basename = 'Mapas' )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculoRota/', CalculoRota),
    path('', include(router.urls))
    
]
