from rest_framework import serializers
from .models import Categoria, Producto


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'


class ReporteProductosSerializer(serializers.Serializer):
    cantidad = serializers.IntegerField()
    producto = ProductoSerializer(many=True)

