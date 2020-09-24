from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator

# Create your views here.

def establecimientos(request):
    if request.method != 'POST':

        lista = Establecimiento.objects.all()
        paginator = Paginator(lista, 5) # Show 25 contacts per page.

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'establecimientos.html', {'lista_colegios': page_obj})
    return redirect(request, 'establecimientos')


def filtro(request):
    if request.method == 'POST':
        if request.POST['busqueda'] != '':
            query = Establecimiento.objects.filter(nombre__icontains=request.POST['busqueda'])
            resultado = {'resultado': query}
            return render(request,'establecimientos.html',resultado)
        else:
           return render(request,'establecimientos.html',{'error_busqueda':'Debes ingresar una palabra clave para buscar'}) 
    #  return redirect('establecimientos')
    

def listing(request):
    
    lista = Establecimiento.objects.all()
    paginator = Paginator(lista, 10) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'establecimientos.html', {'lista_colegios': page_obj})

def info_establecimientos(request):
    pass