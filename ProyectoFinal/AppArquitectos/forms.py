from dataclasses import field
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    password1: forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2: forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {k:"" for k in fields}