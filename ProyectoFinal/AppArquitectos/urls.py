from inspect import formatannotationrelativeto
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('edificio/', EdificioList.as_view(), name = "edificio"),
    path('', inicio, name = "inicio"),
    path('crearedificio/', crearedificio, name='crearedificio'),
    path('busqueda/edificio/',busqueda_edificio, name='busqueda_edificio'),
    path('buscar/', buscar),
    path('arquitecto/', ArquitectoList.as_view(), name= 'arquitecto_listar'),
    path("arquitecto/<pk>", ArquitectoDetalle.as_view(), name= 'arquitecto_detalle' ),
    path('arquitecto/nuevo/', ArquitectoCreacion.as_view(), name= 'arquitecto_crear'),
    path('arquitecto/editar/<pk>', Arquitectoupdate.as_view(), name= 'arquitecto_editar'),  
    path('arquitecto/borrar/<pk>', ArquitectoDelete.as_view(), name= 'arquitecto_borrar'),
    path('logout/', LogoutView.as_view(template_name='AppArquitectos/logout.html'), name='logout'),
  ]