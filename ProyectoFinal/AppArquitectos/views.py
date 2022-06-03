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
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ArquitectoList(ListView):
    model=Arquitecto
    template_name = "AppArquitectos/arquitecto.html"

class ArquitectoDetalle(DetailView):
    model = Arquitecto
    template_name = "AppArquitectos/arquitecto_detalle.html"

class ArquitectoCreacion(CreateView):
    model = Arquitecto
    success_url = reverse_lazy('arquitecto_listar')
    fields = ['nombre','matricula','telefono']

class Arquitectoupdate(UpdateView):
    model = Arquitecto
    success_url = reverse_lazy('arquitecto_listar')
    fields = ['nombre','matricula','telefono']

class ArquitectoDelete(DeleteView):
    model = Arquitecto
    success_url = reverse_lazy('arquitecto_listar')


def consultas(request):
    return render(request, "AppArquitectos/consulta.html")

def ConsultaEnviada(request):
    return render(request, "AppArquitectos/ConsultaEnviada.html")


class ConsultaCreacion(LoginRequiredMixin,CreateView):
    model = Consulta
    success_url = reverse_lazy('ConsultaEnviada')
    fields = ['nombre','consulta','telefono','email']

#def crearconsulta(request):
    #if request.method == 'POST':
         #formulario = ConsultaFormulario(request.POST)
         #if formulario.is_valid():
             #informacion = formulario.cleaned_data
             #consultarealizada= Consulta(nombre= informacion['nombre'], consulta= informacion['consulta'], telefono= informacion['telefono'], email= informacion['email'])
             #consultarealizada.save()
             #return render(request, "AppArquitectos/ConsultaEnviada.html")
     #else:
         #formulario = ConsultaFormulario()      
    #return render(request,"AppArquitectos/crearconsulta.html",{'formulario':formulario})



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
            return render(request, "AppArquitectos/bienvenida.html", {'mensaje1': f'Usuario {username} Creado'})
        else:
            return render(request, "AppArquitectos/registro.html", {'form':form,'mensaje2': "NO SE PUDO CREAR EL USUARIO"})
    
    else:
        form= UserRegisterForm()
        return render(request, "AppArquitectos/registro.html", {"form":form})
