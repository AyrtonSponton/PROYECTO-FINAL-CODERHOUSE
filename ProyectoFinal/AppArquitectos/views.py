from dataclasses import field, fields
from django.http import HttpResponse
from django.shortcuts import render
from .models import Arquitecto, Edificio, Consulta
from AppArquitectos.forms import ArquitectoFormulario, ConsultaFormulario, EdificioFormulario, UserRegisterForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
# Create your views here.

class ArquitectoList(ListView):
    model=Arquitecto
    template_name= "AppArquitectos/arquitecto.html"

class ArquitectoCreacion(CreateView):
    model=Arquitecto
    succese_url = reverse_lazy('arquitecto_listar')
    fields= ['nombre', 'matricula', 'telefono']

class ArquitectoEditar(UpdateView):
    model=Arquitecto
    success_url= reverse_lazy('arquitecto_listar')
    fields= ['nombre', 'matricula', 'telefono']

class ArquitectoBorrar(DeleteView):
    model=Arquitecto
    succese_url = reverse_lazy('arquitecto_listar')


def consultas(request):
    return render(request, "AppArquitectos/consulta.html")



def crearconsulta(request):
    if request.method == 'POST':
        formulario = ConsultaFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            consultarealizada= Consulta(nombre= informacion['nombre'], consulta= informacion['consulta'], telefono= informacion['telefono'], email= informacion['email'])
            consultarealizada.save()
            return render(request, "AppArquitectos/ConsultaEnviada.html")
    else:
        formulario = ConsultaFormulario()      
    return render(request,"AppArquitectos/crearconsulta.html",{'formulario':formulario})



def edificio(request):
    return render(request, "AppArquitectos/edificio.html")



def crearedificio(request):
    if request.method == 'POST':
        formulario = EdificioFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            edificio= Edificio (nombre= informacion['nombre'], ubicacion= informacion['ubicacion'])
            edificio.save()
            return render(request, "AppArquitectos/Edificiocreado.html")
    else:
        formulario = EdificioFormulario()      
    return render(request,"AppArquitectos/crearedificio.html",{'formulario':formulario})

def busqueda_edificio(request):
    return render(request, "AppArquitectos/busqueda_edificio.html")

def buscar(request):
    if request.GET['edificio']:
        edificio= request.GET['edificio']
        edificios= Edificio.objects.filter(nombre = edificio)
        return render (request, "AppArquitectos/resultadobusqueda.html", {"Nombre": edificios})
    
    else:
        respuesta = "Ingrese datos validos"
        return HttpResponse(respuesta)

def inicio(request):
    return render(request, "AppArquitectos/inicio.html")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user= form.cleaned_data.get('usuario')
            contra= form.cleaned_data.get('contraseña')

            Usuario= authenticate(username = user, password = contra)

            if Usuario is not None:
                login(request, Usuario)
                return render(request, "AppArquitectos/inicio.html",{"mensaje": f"Bienvenido {user}"})
            else:
                return render(request, "AppArquitectos/inicio.html", {"mensaje": "Error, Datos Incorrectos"} )
        
        else:
            return render(request, "AppArquitectos/inicio.html", {"mensaje": "Error, Formulario Incorrecto"} )

    form = AuthenticationForm()
    return render(request,"AppArquitectos/login.html", {'form':form})


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():

            username= form.cleaned_data['username']
            form.save()
            return render(request, "AppArquitectos/registro.html", {"mensaje": f"Usuario {username} Creado"})
    
    else:
        form= UserRegisterForm()
        return render(request, "AppArquitectos/registro.html", {"form":form})

@login_required
def consulta(request):
    return render(request, "AppArquitectos/consulta.html")