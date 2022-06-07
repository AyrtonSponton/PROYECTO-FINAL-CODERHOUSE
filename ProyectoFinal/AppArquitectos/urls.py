from inspect import formatannotationrelativeto
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('inicio/', inicio, name = "inicio"),
    path('edificio/', EdificioList.as_view(), name = "edificio"),
    path('edificio/nuevo/', EdificioCrear.as_view(), name='edificio_crear'),
    path('edificio/<pk>', EdificioDetalle.as_view(), name='edificio_detalle'),
    path('edificio/editar/<pk>', EdificioUpdate.as_view(), name= 'edificio_editar'),  
    path('edificio/borrar/<pk>', EdificioDelete.as_view(), name= 'edificio_borrar'),
    path('arquitecto/', ArquitectoList.as_view(), name= 'arquitecto_listar'),
    path("arquitecto/<pk>", ArquitectoDetalle.as_view(), name= 'arquitecto_detalle' ),
    path('arquitecto/nuevo/', ArquitectoCreacion.as_view(), name= 'arquitecto_crear'),
    path('arquitecto/editar/<pk>', Arquitectoupdate.as_view(), name= 'arquitecto_editar'),  
    path('arquitecto/borrar/<pk>', ArquitectoDelete.as_view(), name= 'arquitecto_borrar'),
    path('logout/', LogoutView.as_view(template_name='AppArquitectos/logout.html'), name='logout'),
  ]
