from django.http import HttpResponse
from django.template import loader, context, Template

def saludo (request):
    return HttpResponse ("<br><br> <h1>Bienvenido a la Pagina de Inicio")

def probandotemplate(request):
    plantilla = loader.get_template('inicio.html')
    documento = plantilla.render(context)
    return HttpResponse(documento)