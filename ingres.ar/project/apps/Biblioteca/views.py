from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
@login_required
def biblioteca(request):
<<<<<<< HEAD
    archivos = Biblioteca.objects.all()
    context = {'archivos_clave': archivos }
=======
    return render(request,'biblioteca.html')

def material(request):
    archivo = Material.objects.all()
    context = {'material_clave': archivo }
>>>>>>> 7d575f995544f4299c9bd6c32e225599840b9c2e
    return render(request,'biblioteca.html',context)