from dataclasses import field
from django import forms
from .models import *


class ArquitectoFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    matricula = forms.IntegerField()
    telefono = forms.IntegerField()

class EdificioFormulario(forms.Form):
    nombre = forms.CharField (max_length=50)
    ubicacion = forms.CharField (max_length=50)
    imagen_edificio = forms.ImageField(label="Imagen")
    imagen_ubicacion = forms.ImageField(label="Imagen Ubicacion")

    class Meta:
        model= Edificio
        fields = ['nombre','ubicacion','imagen_edificio','imagen_ubicacion']


