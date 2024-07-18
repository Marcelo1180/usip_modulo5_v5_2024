from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Categoria, Producto
from .form import ProductForm
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .serializers import CategoriaSerializer, ProductoSerializer
from rest_framework import generics
from rest_framework.decorators import api_view


def index(request):
    return HttpResponse("Hola Mundo")

def contact(request, name):
    return HttpResponse(f"Bienvenido {name} a la clase de hoy")

def categorias(request):
    post_nombre = request.POST.get("nombre")
    if post_nombre:
        q = Categoria(nombre=post_nombre)
        q.save()

    filtro_nombre = request.GET.get("nombre")
    if filtro_nombre:
        categorias = Categoria.objects.filter(nombre__contains=filtro_nombre)
    else:
        categorias = Categoria.objects.all()
    return render(request, "form_categorias.html", {"categorias": categorias})

def productoFormView(request):
    form = ProductForm()
    producto = None
    id_producto = request.GET.get("id")
    if id_producto:
        # producto = Producto.objects.get(id=10011)
        producto = get_object_or_404(Producto, id=id_producto)
        form = ProductForm(instance=producto)

    if request.method == "POST":
        if producto:
            form = ProductForm(request.POST, instance=producto)
        else:
            form = ProductForm(request.POST)

    if form.is_valid():
        form.save()

    return render(request, "form_productos.html", {"form": form})


class CategoriasViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CategoriaCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

@api_view(['GET'])
def categoria_count(request):
    """
    Cuenta la cantidad de __categorias__
    """

    try:
        cantidad = Categoria.objects.count()
        return JsonResponse(
            {
                "cantidad": cantidad
            },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse(
            {
                "error": str(e)
            },
            safe=False,
            status=400
        )


@api_view(['GET'])
def productos_en_unidades(requesto):
    """
    Lista de productos filtrados en unidades
    """

    try:
        productos = Producto.objects.filter(unidades='u')
        return JsonResponse(
            ProductoSerializer(productos, many=True).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse(
            {
                "error": str(e)
            },
            safe=False,
            status=400
        )
