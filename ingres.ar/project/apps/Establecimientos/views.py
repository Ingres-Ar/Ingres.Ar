from django.shortcuts import render
from .models import *
# Create your views here.

def establecimientos(request):
    colegios = Establecimiento.objects.all()
    context = {'colegios_clave': colegios }
    return render(request,'establecimientos.html',context)