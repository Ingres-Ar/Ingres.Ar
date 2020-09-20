from django.shortcuts import render
from django.contrib.auth.models import User
# from . import models

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
            return render(request, 'home.html',{'error':'Algunos datos no son correctos!'})
            # return redirect('home')
    
    # return render(request, '../../Biblioteca/templates/biblioteca.html')  

def register_view(request):
    # import pdb; pdb.set_trace()
    if request.method == 'POST':
        usuario = request.POST['username']
        password = request.POST['password']
        email  = request.POST['email']
        confirm_pass = request.POST['confirm_pass']
        if confirm_pass != password:
            return render(request, 'registro.html') 
        user = User.objects.create_user(usuario, email,password )
    return render(request, 'registro.html') 


@login_required
def logout_view(request):
    # logout(request)
    return redirect('home')
