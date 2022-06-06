from dataclasses import field, fields
from django.http import HttpResponse
from django.shortcuts import render
from .models import Arquitecto, Edificio
from AppArquitectos.forms import EdificioFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
class ArquitectoList(ListView):
    model=Arquitecto
    template_name = "AppArquitectos/arquitecto.html"

class ArquitectoDetalle(DetailView):
    model = Arquitecto
    template_name = "AppArquitectos/arquitecto_detalle.html"

class ArquitectoCreacion(CreateView):
    model = Arquitecto
    success_url = reverse_lazy('agregaravatar')
    fields = ['nombre','matricula','telefono']

class Arquitectoupdate(UpdateView):
    model = Arquitecto
    success_url = reverse_lazy('arquitecto_listar')
    fields = ['nombre','matricula','telefono']

class ArquitectoDelete(DeleteView):
    model = Arquitecto
    success_url = reverse_lazy('arquitecto_listar')
    

class EdificioList(ListView):
    model=Edificio
    template_name = "AppArquitectos/edificio.html"


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
    if request.user.is_authenticated:
        avatar=Avatar.objects.filter(user=request.user)
        return render(request, 'AppArquitectos/inicio.html', {'url': avatar[0].avatar.url})
    else:
        return render(request, 'AppArquitectos/inicio.html')


