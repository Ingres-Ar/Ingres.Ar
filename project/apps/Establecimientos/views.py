from django.shortcuts import render

# Create your views here.

def establecimientos(request):
    return render(request,'../templates/establecimientos.html')