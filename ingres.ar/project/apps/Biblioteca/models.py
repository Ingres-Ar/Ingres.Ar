from django.db import models

class Material(models.Model):
    nombre = models.CharField(max_length=170)
    enlace = models.CharField(max_length=500)