from inspect import formatannotationrelativeto
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('edificio/', edificio, name = "edificio"),
    path('consulta/', consultas, name = "consulta"),
    path('', inicio, name = "inicio"),
    path('crearedificio/', crearedificio, name='crearedificio'),
    path('consulta/nuevo', ConsultaCreacion.as_view(), name='crearconsulta'),
    path('busqueda/edificio/',busqueda_edificio, name='busqueda_edificio'),
    path('buscar/', buscar),
    path('ConsultaEnviada/',ConsultaEnviada, name='ConsultaEnviada'),
    path('arquitecto/', ArquitectoList.as_view(), name= 'arquitecto_listar'),
    path("arquitecto/<pk>", ArquitectoDetalle.as_view(), name= 'arquitecto_detalle' ),
    path('arquitecto/nuevo/', ArquitectoCreacion.as_view(), name= 'arquitecto_crear'),
    path('arquitecto/editar/<pk>', Arquitectoupdate.as_view(), name= 'arquitecto_editar'),  
    path('arquitecto/borrar/<pk>', ArquitectoDelete.as_view(), name= 'arquitecto_borrar'),
    path('login/', login_request, name='login'),
    path('registro/', register, name='registro'),
    path('logout/', LogoutView.as_view(template_name='AppArquitectos/logout.html'), name='logout'),
  ]