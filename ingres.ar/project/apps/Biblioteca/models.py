from django.db import models

<<<<<<< HEAD
# Create your models here.

class Biblioteca(models.Model):
    nombre = models.CharField(max_length=100)
    link = models.CharField(max_length=100)

=======
class Material(models.Model):
    nombre = models.CharField(max_length=170)
    enlace = models.CharField(max_length=500)
>>>>>>> 7d575f995544f4299c9bd6c32e225599840b9c2e
