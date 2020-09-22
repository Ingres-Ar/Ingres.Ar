from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
@login_required
def biblioteca(request):
    archivos = Biblioteca.objects.all()
    context = {'archivos_clave': archivos }
    return render(request,'biblioteca.html',context)