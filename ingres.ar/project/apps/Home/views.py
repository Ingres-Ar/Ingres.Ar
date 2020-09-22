from django.shortcuts import render

# Create your views here.

def home(request):
    # import pdb; pdb.set_trace()
    return render(request,'home.html')