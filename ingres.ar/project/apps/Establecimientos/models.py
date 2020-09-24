from django.db import models

class Establecimiento(models.Model):
    cue = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    nombre = models.CharField(max_length=150)
    nro_escuela = models.IntegerField(null=True)

class Localizacion(models.Model):
    anexo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    establecimiento = models.ForeignKey(
                                Establecimiento,
                                on_delete=models.CASCADE)

class Domicilio(models.Model):
    calle = models.CharField(max_length=50)
    altura = models.IntegerField()
    departamento = models.CharField(max_length=50)
    localizacion = models.ForeignKey(Localizacion,
                                    on_delete=models.CASCADE)

class Oferta(models.Model):
    modalidad = models.CharField(max_length=100)
    nivel = models.CharField(max_length=50)
    establecimiento = models.ManyToManyField(Establecimiento)

class Orientacion(models.Model):
    especialidad = models.CharField(max_length=100)
    oferta = models.ManyToManyField(Oferta)
