from inspect import formatannotationrelativeto
from xml.etree.ElementInclude import include
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('consulta/', consultas, name = "consulta"),
    path('consulta/nuevo', ConsultaCreacion.as_view(), name='crearconsulta'),
    path('ConsultaEnviada/',ConsultaEnviada, name='ConsultaEnviada'),
    path('login/', login_request, name='login'),
    path('registro/', register, name='registro'),
    path('editarperfil/', editarperfil, name='editarperfil'),
    path('agregaravatar/', agregarAvatar, name='agregaravatar'),
    path('inicio2/', inicio, name = "inicio2"),
  ]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)