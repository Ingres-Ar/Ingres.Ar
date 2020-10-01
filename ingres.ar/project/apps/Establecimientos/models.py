from django.db import models

class Establecimiento(models.Model):
    id_establecimiento = models.CharField(max_length=100, primary_key=True)
    cue = models.CharField(max_length=7,null=True)
    sector = models.CharField(max_length=10)
    nombre = models.CharField(max_length=150)

class Localizacion(models.Model):
    id_localizacion = models.CharField(max_length=100, primary_key=True)
    anexo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    establecimiento = models.ForeignKey(
                                Establecimiento,
                                on_delete=models.CASCADE)

class Domicilio(models.Model):
    id_domicilio = models.CharField(max_length=100,primary_key=True)
    calle = models.CharField(max_length=50)
    altura = models.IntegerField()
    # departamento = models.CharField(max_length=50) se quita dpto
    barrio = models.CharField(max_length=50)
    id_localizacion = models.ManyToManyField(Localizacion)

class Oferta(models.Model):
    modalidad = models.CharField(max_length=100)
    nivel = models.CharField(max_length=50)
    establecimiento = models.ManyToManyField(Establecimiento)

class Orientacion(models.Model):
    especialidad = models.CharField(max_length=100)
    oferta = models.ManyToManyField(Oferta)
