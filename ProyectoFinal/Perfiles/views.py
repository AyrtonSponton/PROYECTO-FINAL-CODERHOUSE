from django.shortcuts import render
from dataclasses import field, fields
from django.http import HttpResponse
from django.shortcuts import render
from .models import Avatar, Consulta
from Perfiles.forms import UserRegisterForm, UserEditForm, AvatarForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
def consultas(request):
    return render(request, "AppArquitectos/consulta.html")

def ConsultaEnviada(request):
    return render(request, "AppArquitectos/ConsultaEnviada.html")

class ConsultaCreacion(LoginRequiredMixin,CreateView):
    model = Consulta
    success_url = reverse_lazy('ConsultaEnviada')
    fields = ['nombre','consulta','telefono','email']


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid():
            usuario= form.cleaned_data.get('username')
            clave= form.cleaned_data.get('password')
            persona= authenticate(username=usuario, password=clave)
            if persona is not None:
                login(request, persona)
                return render(request, "AppArquitectos/bienvenida.html",{'mensaje1': f'Bienvenido al sistema {usuario}'})
            else:
                return render(request, "AppArquitectos/login.html", {'form':form,'mensaje3':'Error, Datos Incorrectos, por favor vuelva a intentarlo'} )    
        else:
            return render(request, "AppArquitectos/login.html", {'form':form,'mensaje4': 'Error, Formulario Incorrecto'} )
    else:
        form = AuthenticationForm()
        return render(request,"AppArquitectos/login.html", {'form':form})


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data['username']
            form.save()
            return render(request, "AppArquitectos/bienvenida.html", {'mensaje1': f'Usuario {username} Creado, Agregue su Avatar'})
        else:
            return render(request, "AppArquitectos/registro.html", {'form':form,'mensaje2': "NO SE PUDO CREAR EL USUARIO"})
    
    else:
        form= UserRegisterForm()
        return render(request, "AppArquitectos/registro.html", {"form":form})


@login_required
def editarperfil(request):
    usuario = request.user
    if request.method == "POST":
        miFormulario = UserEditForm(request.POST, instance=usuario)
        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()
            return render(request, "AppArquitectos/bienvenida.html", {'mensaje2': 'Datos Cambiados'})
        else:
            return render(request, "AppArquitectos/login.html", {'miFormulario':miFormulario,'mensaje3':'Error, Datos Incorrectos, por favor vuelva a intentarlo'})
    else:
        miFormulario=UserEditForm(initial = {'email':usuario.email})
        return render(request, "AppArquitectos/editarperfil.html", {'miFormulario':miFormulario, 'usuario':usuario} )

@login_required
def agregarAvatar(request):
    if request.method =='POST':
        usuario = User.objects.get(username=request.user)
        formulario=AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            avatarsito = Avatar(user=usuario, avatar=formulario.cleaned_data['avatar'])
            avatarsito.save()
            return render(request, 'AppArquitectos/agregaravatar.html',{'mensaje': 'Avatar Agregado'})
        else:
            return render(request, 'AppArquitectos/agregaravatar.html', {'mensaje2': 'Error, vuelva a intentarlo'})
    else:
        formulario=AvatarForm()
    return render(request, 'AppArquitectos/agregaravatar.html', {'formulario':formulario})