from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"core/home.html")

def historia(request):
    return render(request,"core/history.html")

def otros(request):
    return render(request,"core/other.html")


def visita(request):
    return render(request,"core/visit.html")

def blogs(request):
    return render(request,"core/blog.html")

def contacto(request):
    return render(request,"core/contacto.html")
    
