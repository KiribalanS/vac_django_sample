from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
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

@csrf_exempt
def form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        print(name)
        return HttpResponse(f"Form Submitted!\nYour name is: {name}")
    else:
        return render(request, 'form.html')

# def myf(request):
#     return