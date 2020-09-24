from django.shortcuts import render
from .models import *
# Create your views here.

def establecimientos(request):
    colegios = Establecimiento.objects.all()
    context = {'colegios_clave': colegios }
    return render(request,'establecimientos.html',context)

def busqueda(request):
    if request.method == 'GET':
        busqueda = request.GET['Establecimiento.objects.filter()']
        context = {'colegios_clave': colegios }
        return render(request, 'establecimientos.html',{'busqueda':'busqueda'})
            # return redirect('home')