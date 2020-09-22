from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def establecimientos(request):
    colegios = Establecimiento.objects.all()
    context = {'colegios_clave': colegios }
    return render(request,'establecimientos.html',context)

def filtro(request):
    if request.method == 'POST':
        query = Establecimiento.objects.filter(nombre__icontains=request.POST['busqueda'])
        resultado = {'resultado': query}
        return render(request,'establecimientos.html',resultado)
    return redirect('establecimientos')