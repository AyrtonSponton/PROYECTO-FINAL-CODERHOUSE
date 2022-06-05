from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Mensaje(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    creado= models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['creado']

class Thread(models.Model):
    users= models.ManyToManyField(User, related_name='threads')
    mensaje= models.ManyToManyField(Mensaje)
