from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class ConsultaFormulario(forms.Form):
    nombre = forms.CharField (max_length= 50)
    consulta = forms.CharField (max_length= 50)
    telefono = forms.IntegerField()
    email = forms.EmailField ()

    
class UserRegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {k:"" for k in fields}


class UserEditForm(UserChangeForm):
    email=forms.EmailField(required=True)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['email','password1','password2']
        help_texts = {k:"" for k in fields}

class AvatarForm(forms.Form):
    avatar= forms.ImageField(label="Avatar")