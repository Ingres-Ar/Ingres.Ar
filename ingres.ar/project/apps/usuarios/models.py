#Modelo customizado de User django llamado perfil.

'''A partir de este modelo se crea una tabla en la base de datos llamada
usuarios_perfil al correr la migracion'''

from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    '''usuario es la relacion entre la table Users y Perfil'''
    usuario = models.OneToOneField(User,on_delete= models.CASCADE)
    telefono = models.CharField(max_length=20,blank=True)
    fecha_nacimiento= models.DateField(null=True)
    foto = models.ImageField(upload_to='media/',blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)


'''solo redefino el método str para observar en shell el nombre de usuario'''
def __str__(self):
    return self.usuario.username