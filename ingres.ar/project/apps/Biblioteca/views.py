from django.shortcuts import render

# Create your views here.

def biblioteca(request):
    return render(request,'../templates/biblioteca.html')