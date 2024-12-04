from mmap import error
from django.db.models import Sum  # Asegúrate de importar Sum correctamente
from django.db.models import Count  # Asegúrate de importar Count

from django.db.models import Sum, Count
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import models
from .models import Producto
from .serializers import ProductoEstadisticasSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from yaml import serialize

from apps.catalogos.producto.models import Producto
from .serializers import ProductoSerializer
from drf_yasg.utils import swagger_auto_schema

class ProductoApiView(APIView):

    @swagger_auto_schema(responses={200: ProductoSerializer(many=True)})
    def get(self, request):

     productos = Producto.objects.all()
     serializer = ProductoSerializer(productos, many=True)
     return Response(serializer.data)

    @swagger_auto_schema(request_body=ProductoSerializer, responses={200: ProductoSerializer})
    def post(self, request):
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductoDetailApiView(APIView):

    @swagger_auto_schema(responses={200: ProductoSerializer})
    def get(self, request, pk:None):
        try:
            producto = Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            return Response({'error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ProductoSerializer, responses={200: ProductoSerializer})
    def put(self, request, pk):

        try:
            producto = Producto.objects.get(pk=pk)
        except producto.DoesNotExist:
            return Response({'error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serialazer = ProductoSerializer(instance=producto, data=request.data)
        if serialazer.is_valid():
            serialazer.save()
            return Response(serialazer.data)
        return Response(serialazer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=ProductoSerializer, responses={200: ProductoSerializer})
    def patch(self, request, pk):
        try:
            producto = Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            return Response({'error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serialazer = ProductoSerializer(instance=producto, data=request.data, partial=True)
        if serialazer.is_valid():
            serialazer.save()
            return Response(serialazer.data)
        return Response(serialazer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'Producto eliminado correctamente'})

    def delete(self, request, pk):
        try:
            producto = Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            return Response({'error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        try:
            producto.delete()
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductoEstadisticasApiView(APIView):
    """
    Vista para obtener estadísticas de productos.
    """

    def get(self, request):
        # Estadísticas principales
        total_activos = Producto.objects.filter(Estado=True).count()
        total_stock = Producto.objects.aggregate(total=Sum('Stock'))['total'] or 0

        # Agrupación por categoría
        productos_por_categoria = (
            Producto.objects.values('categoria__Descripcion')  # Ajusta si 'Descripcion' no es correcto
            .annotate(count=Count('id'))
            .order_by('categoria__Descripcion')
        )
        productos_por_categoria_dict = {item['categoria__Descripcion']: item['count'] for item in productos_por_categoria}

        # Datos a devolver
        data = {
            "total_activos": total_activos,
            "total_stock": total_stock,
            "productos_por_categoria": productos_por_categoria_dict,
        }

        return Response(data, status=status.HTTP_200_OK)


# from django.urls import path
# from .views import ProductoApiView, ProductoDetailApiView
# app_name = 'producto'
#
# urlpatterns = [
#     path('productos/', ProductoApiView.as_view(), name='api_producto'),
#     path('<int:pk>/', ProductoDetailApiView.as_view()),
# ]