from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from AppArquitectos.forms import ArquitectoFormulario, ConsultaFormulario, EdificioFormulario

# Create your views here.
def arquitecto(request):
    return render(request,"AppArquitectos/arquitecto.html")



def creararquitecto(request):
    if request.method == 'POST':
        formulario = ArquitectoFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            arquitecto= arquitectos (nombre= informacion['nombre'], matricula= informacion['matricula'], telefono= informacion['telefono'])
            arquitecto.save()
            return render(request, "AppArquitectos/Arquicreado.html")
    else:
        formulario = ArquitectoFormulario()      
    return render(request,"AppArquitectos/creararquitecto.html",{'formulario':formulario})



def consultas(request):
    return render(request, "AppArquitectos/consulta.html")



def crearconsulta(request):
    if request.method == 'POST':
        formulario = ConsultaFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            consultarealizada= consulta(nombre= informacion['nombre'], consulta= informacion['consulta'], telefono= informacion['telefono'], email= informacion['email'])
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
            edificio= edificios (nombre= informacion['nombre'], ubicacion= informacion['ubicacion'])
            edificio.save()
            return render(request, "AppArquitectos/Edificiocreado.html")
    else:
        formulario = EdificioFormulario()      
    return render(request,"AppArquitectos/crearedificio.html",{'formulario':formulario})



def inicio(request):
    return render(request, "AppArquitectos/inicio.html")

def busqueda(request):
    return render(request, "AppArquitectos/busqueda_arquitecto.html")

def buscar_arquitecto(request):
    if request.GET['matricula']:
        matricula= request.GET['matricula']
        arquitecto = arquitectos.objects.filter(matricula__icontains= matricula)

        return render(request, "AppArquitectos/busqueda_arquitecto.html",{"Arquitecto": arquitecto, "matricula": matricula})
    else:
        respuesta = "Ingrese nuevamente los datos"

    return HttpResponse(respuesta)