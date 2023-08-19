from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse(" WELCOME")
def shop(request):
    return HttpResponse("Welcome to SHOP")
def aakash(request,name):
    return render(request,'index.html',context={'Kowshik':name})

def loop(request):
    return render(request,'loop.html',context={'range':range(5)})
