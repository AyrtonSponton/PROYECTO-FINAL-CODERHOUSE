from dataclasses import field, fields
from django.http import HttpResponse
from django.shortcuts import render
from .models import Arquitecto, Edificio
from AppArquitectos.forms import EdificioFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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
    

class EdificioList(ListView):
    model=Edificio
    template_name = "AppArquitectos/edificio.html"


class EdificioCrear(CreateView):
    model=Edificio
    success_url = reverse_lazy('edificio')
    fields = ['nombre','ubicacion','imagen_edificio','imagen_ubicacion']

class EdificioDetalle(DetailView):
    model = Edificio
    template_name = "AppArquitectos/edificio_detalle.html"

class EdificioUpdate(UpdateView):
    model=Edificio
    success_url = reverse_lazy('edificio')
    fields = ['nombre','ubicacion','imagen_edificio','imagen_ubicacion']

class EdificioDelete(DeleteView):
    model = Edificio
    success_url = reverse_lazy('edificio')

def inicio(request):
    return render(request, 'AppArquitectos/inicio.html')


