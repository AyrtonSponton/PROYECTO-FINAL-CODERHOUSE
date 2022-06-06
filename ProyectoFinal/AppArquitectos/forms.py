from dataclasses import field
from django import forms


class ArquitectoFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    matricula = forms.IntegerField()
    telefono = forms.IntegerField()

class EdificioFormulario(forms.Form):
    nombre = forms.CharField (max_length=50)
    ubicacion = forms.CharField (max_length=50)


