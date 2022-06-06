from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar', null=True, blank = True)

class Consulta(models.Model):
    nombre = models.CharField(max_length= 50)
    consulta = models.CharField(max_length= 50)
    telefono = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.nombre+" "+"Consulta:"+self.consulta+" "+"Telefono:"+" "+str(self.telefono)+" "+"email:"+" "+self.email

        