from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        usuario = authenticate(request,username=username,password=password)
        if usuario:
            login(request,usuario)
            return redirect('home')
        else:
            return render(request, '../../Home/templates/home.html',{'error':'Algunos datos no son correctos!'})
            # return redirect('home')
    
    return render(request, '../../Biblioteca/templates/biblioteca.html')  #solo es de prueba

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')
