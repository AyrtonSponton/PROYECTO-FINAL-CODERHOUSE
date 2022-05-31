from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField

# Create your models here.
class Arquitecto(models.Model):
    nombre = models.CharField(max_length=50)
    matricula = models.IntegerField()
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre+" "+"Matricula:"+str(self.matricula)+" "+"Telefono:"+str(self.telefono)

class Consulta(models.Model):
    nombre = models.CharField(max_length= 50)
    consulta = models.CharField(max_length= 50)
    telefono = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.nombre+" "+"Consulta:"+self.consulta+" "+"Telefono:"+" "+str(self.telefono)+" "+"email:"+" "+self.email


class Edificio (models.Model):
    nombre = models.CharField (max_length=50)
    ubicacion = models.CharField (max_length=50) 
    
    def __str__(self):
        return "Nombre del Edificio:"+" "+self.nombre+" "+"Ubicacion:"+" "+self.ubicacion
