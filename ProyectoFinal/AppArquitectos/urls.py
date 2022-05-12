from inspect import formatannotationrelativeto
from django.urls import path
from .views import arquitecto, consultas, edificio, consultas, inicio, creararquitecto, crearedificio, crearconsulta,busqueda,buscar_arquitecto

urlpatterns = [
    path('arquitecto/', arquitecto, name = "arquitecto"),
    path('edificio/', edificio, name = "edificio"),
    path('consulta/', consultas, name = "consulta"),
    path('', inicio, name = "inicio"),
    path('creararquitecto/', creararquitecto, name='creararquitecto'),
    path('crearedificio/', crearedificio, name='crearedificio'),
    path('crearconsulta/', crearconsulta, name='crearconsulta'),
    path('busqueda/',busqueda, name='busqueda'),
    path('buscar_arquitecto/',buscar_arquitecto, name='buscar_arquitecto')
  ]