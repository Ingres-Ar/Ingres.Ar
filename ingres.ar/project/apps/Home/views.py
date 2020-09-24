from django.shortcuts import render

# Create your views here.

def home(request):
    context = {'error_1': 'Registrate para acceder a la Biblioteca',
    'error_2': 'Registrate para acceder a la Autoevaluacion',
       }
    return render(request,'home.html',context)