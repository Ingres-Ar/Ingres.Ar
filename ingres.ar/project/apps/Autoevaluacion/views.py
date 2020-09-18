from django.shortcuts import render

# Create your views here.

def autoevaluacion(request):
    return render(request,'../templates/Autoevaluacion.html')