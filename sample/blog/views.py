from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Lunch Time")

def shop(request):
    return HttpResponse("Shop VCET")

def college(request):
    return HttpResponse("Velalar college of engineering and technology")

def html(request):
    return render(request, 'index.html')
def form(request):
    return render(request, 'form.html')

def text(request):
    return render(request, 'text.html',
                   context= {
        "text": "the context text"
    })

def para(request, name):
    return render(
        request, 'url.html',
        context={
            "url": name
        }
    )

def myf(request):
    name = request.POST.get("name")
    print(name)
    return HttpResponse("Form Submitted!")
