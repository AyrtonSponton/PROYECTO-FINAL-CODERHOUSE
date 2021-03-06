from unittest.util import _MAX_LENGTH
from django.db import models


# Create your models here.
class Arquitecto(models.Model):
    nombre = models.CharField(max_length=50)
    matricula = models.IntegerField()
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre+" "+"Matricula:"+str(self.matricula)+" "+"Telefono:"+str(self.telefono)

class Edificio (models.Model):
    nombre = models.CharField (max_length=50)
    ubicacion = models.CharField (max_length=50) 
    imagen_edificio = models.ImageField(upload_to='Imagen_Edificio',null= True, blank = True)
    imagen_ubicacion = models.ImageField(upload_to='imagen_ubicacion', null= True, blank = True)
    
    def __str__(self):
        return "Nombre del Edificio:"+" "+self.nombre+" "+"Ubicacion:"+" "+self.ubicacion



