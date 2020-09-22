from django.db import models

# Create your models here.

class Biblioteca(models.Model):
    nombre = models.CharField(max_length=100)
    link = models.CharField(max_length=100)

