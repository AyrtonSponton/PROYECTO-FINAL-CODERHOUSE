from django import forms

class ArquitectoFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    matricula = forms.IntegerField()
    telefono = forms.IntegerField()

class ConsultaFormulario(forms.Form):
    nombre = forms.CharField (max_length= 50)
    consulta = forms.CharField (max_length= 50)
    telefono = forms.IntegerField()
    email = forms.EmailField ()

class EdificioFormulario(forms.Form):
    nombre = forms.CharField (max_length=50)
    ubicacion = forms.CharField (max_length=50)