from django.shortcuts import render
from .models import *
# Create your views here.

def establecimientos(request):
    colegios = Establecimiento.objects.all()
    context = {'colegios_clave': colegios }
    return render(request,'establecimientos.html',context)

def filtro(request):
    if request.method == 'POST':
        if request.POST['busqueda'] != '':
            query = Establecimiento.objects.filter(nombre__icontains=request.POST['busqueda'])
            resultado = {'resultado': query}
            return render(request,'establecimientos.html',resultado)
        else:
           return render(request,'establecimientos.html',{'error_busqueda':'Debes ingresar una palabra clave para buscar'}) 
    return redirect('establecimientos')