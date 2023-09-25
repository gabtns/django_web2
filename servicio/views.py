from django.shortcuts import render
from .models import servicios
# Create your views here.
def serv(request):
    objetivos = servicios.objects.all()
    print(objetivos)
    return render(request,"servicio/service.html",{"servicios": objetivos})