from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        usuario = authenticate(request,username=username,password=password)
        if usuario:
            login(request,usuario)
            return redirect('biblioteca')
        else:
            return render(request, '../../Home/templates/home.html',{'error':'Algunos datos no son correctos!'})
            # return redirect('home')
    
    return render(request, '../../Biblioteca/templates/biblioteca.html')