from inspect import formatannotationrelativeto
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('consulta/', consultas, name = "consulta"),
    path('consulta/nuevo', ConsultaCreacion.as_view(), name='crearconsulta'),
    path('ConsultaEnviada/',ConsultaEnviada, name='ConsultaEnviada'),
    path('login/', login_request, name='login'),
    path('registro/', register, name='registro'),
    path('logout/', LogoutView.as_view(template_name='AppArquitectos/logout.html'), name='logout'),
    path('editarperfil/', editarperfil, name='editarperfil'),
    path('agregaravatar/', agregarAvatar, name='agregaravatar'),
  ]