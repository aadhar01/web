from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#something that user wants to see

def index(request):
    return render(request, "hello/hello.html")

def aadhar(request):
    return HttpResponse("Hello, Aadhar!!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
    
    
    