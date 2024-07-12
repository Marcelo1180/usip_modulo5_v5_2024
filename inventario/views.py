from django.shortcuts import render
from django.http import HttpResponse
from .models import Categoria


def index(request):
    return HttpResponse("Hola Mundo")

def contact(request, name):
    return HttpResponse(f"Bienvenido {name} a la clase de hoy")

def categorias(request):
    filtro_nombre = request.GET.get("nombre")
    print(filtro_nombre) 
    items = Categoria.objects.all() 
    if filtro_nombre:
        items = Categoria.objects.filter(nombre__icontains=filtro_nombre) 
        

    return render(request, "categorias.html", {"categorias": items})
