from django.shortcuts import render
from dataclasses import field, fields
from django.http import HttpResponse
from django.shortcuts import render
from .models import Avatar, Consulta
from Perfiles.forms import UserRegisterForm, UserEditForm, AvatarForm, ConsultaFormulario
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
def consultas(request):
    return render(request, "Perfiles/consulta.html")

def ConsultaEnviada(request):
    return render(request, "Perfiles/ConsultaEnviada.html")

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
                return render(request, "Perfiles/bienvenida.html",{'mensaje1': f'Bienvenido al sistema {usuario}'})
            else:
                return render(request, "Perfiles/login.html", {'form':form,'mensaje3':'Error, Datos Incorrectos, por favor vuelva a intentarlo'} )    
        else:
            return render(request, "Perfiles/login.html", {'form':form,'mensaje4': 'Error, Formulario Incorrecto'} )
    else:
        form = AuthenticationForm()
        return render(request,"Perfiles/login.html", {'form':form})


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data['username']
            form.save()
            return render(request, "Perfiles/bienvenida.html", {'mensaje1': f'Usuario {username} Creado, Agregue su Avatar'})
        else:
            return render(request, "Perfiles/registro.html", {'form':form,'mensaje2': "NO SE PUDO CREAR EL USUARIO"})
    
    else:
        form= UserRegisterForm()
        return render(request, "Perfiles/registro.html", {"form":form})


@login_required
def editarperfil(request):
    usuario = request.user
    if request.method == "POST":
        miFormulario = UserEditForm(request.POST, instance=usuario)
        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            usuario.email=informacion['email']
            usuario.set_password(informacion['password1'])
            usuario.save()
            return render(request, "Perfiles/bienvenida.html", {'mensaje2': 'Datos Cambiados'})
        else:
            return render(request, "Perfiles/login.html", {'miFormulario':miFormulario,'mensaje3':'Error, Datos Incorrectos, por favor vuelva a intentarlo'})
    else:
        miFormulario=UserEditForm(instance=usuario)
    return render(request, "Perfiles/editarperfil.html", {'miFormulario':miFormulario, 'usuario':usuario} )

@login_required
def agregarAvatar(request):
    if request.method=='POST':
        avatarform=AvatarForm(request.POST, request.FILES)
        if avatarform.is_valid():
            avatarviejo=Avatar.objects.filter(user=request.user)
            if avatarviejo:
                avatarviejo.delete()
            u=User.objects.get(username=request.user)
            avatar=Avatar(user=u,avatar=avatarform.cleaned_data['avatar'])
            avatar.save()
            return render(request, 'Perfiles/bienvenida.html',{"mensaje":f"avatar agregado exitosamente"})
    else:
        avatarform=AvatarForm()
        return render (request,'Perfiles/agregaravatar.html',{'form':avatarform})

@login_required
def inicio(request):
    avatar=Avatar.objects.filter(user=request.user)
    if request.user.is_authenticated:
        return render(request, 'Perfiles/inicio2.html', {'url': avatar[0].avatar.url})
