from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
@login_required
def biblioteca(request):
    return render(request,'biblioteca.html')

def material(request):
    archivo = Material.objects.all()
    context = {'material_clave': archivo }
    return render(request,'biblioteca.html',context)