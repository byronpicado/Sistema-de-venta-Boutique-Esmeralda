from mmap import error

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from yaml import serialize

from apps.catalogos.proveedor.models import Proveedor
from .serializers import ProveedorSerializer
from drf_yasg.utils import swagger_auto_schema

class ProveedorApiView(APIView):

    @swagger_auto_schema(responses={200: ProveedorSerializer(many=True)})
    def get(self, request):

     proveedores = Proveedor.objects.all()
     serializer = ProveedorSerializer(proveedores, many=True)
     return Response(serializer.data)

    @swagger_auto_schema(request_body=ProveedorSerializer, responses={200: ProveedorSerializer})
    def post(self, request):
        serializer = ProveedorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProveedorDetailApiView(APIView):

    @swagger_auto_schema(responses={200: ProveedorSerializer})
    def get(self, request, pk:None):
        try:
            proveedor = Proveedor.objects.get(pk=pk)
        except Proveedor.DoesNotExist:
            return Response({'error': 'Proveedor no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProveedorSerializer(proveedor)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ProveedorSerializer, responses={200: ProveedorSerializer})
    def put(self, request, pk):

        try:
            proveedor = Proveedor.objects.get(pk=pk)
        except proveedor.DoesNotExist:
            return Response({'error': 'Proveedor no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serialazer = ProveedorSerializer(instance=proveedor, data=request.data)
        if serialazer.is_valid():
            serialazer.save()
            return Response(serialazer.data)
        return Response(serialazer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=ProveedorSerializer, responses={200: ProveedorSerializer})
    def patch(self, request, pk):
        try:
            proveedor = Proveedor.objects.get(pk=pk)
        except Proveedor.DoesNotExist:
            return Response({'error': 'Proveedor no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serialazer = ProveedorSerializer(instance=proveedor, data=request.data, partial=True)
        if serialazer.is_valid():
            serialazer.save()
            return Response(serialazer.data)
        return Response(serialazer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'Proveedor eliminado correctamente'})

    def delete(self, request, pk):
        try:
            proveedor = Proveedor.objects.get(pk=pk)
        except Proveedor.DoesNotExist:
            return Response({'error': 'Proveedor no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        try:
            proveedor.delete()
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(status=status.HTTP_204_NO_CONTENT)
class ProveedorEstadoApiView(APIView):
    """
    Vista para filtrar proveedores por estado (activos/inactivos) y contarlos.
    """

    @swagger_auto_schema(
        responses={200: "Lista de proveedores filtrados y su conteo"},
        operation_summary="Filtrar y contar proveedores por estado",
        operation_description="Devuelve una lista de proveedores activos o inactivos según el estado proporcionado y su conteo total."
    )
    def get(self, request, estado):
        """
        Filtra y cuenta proveedores según su estado.

        Parámetros:
        - estado: Booleano (True para activos, False para inactivos).

        Retorna:
        - Lista de proveedores filtrados.
        - Conteo total de proveedores filtrados.
        """
        # Convertir el estado recibido a un booleano
        if estado.lower() in ["true", "1", "activo"]:
            estado_filtrado = True
        elif estado.lower() in ["false", "0", "inactivo"]:
            estado_filtrado = False
        else:
            return Response(
                {"error": "El parámetro 'estado' debe ser 'true/activo' o 'false/inactivo'."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Filtrar los proveedores según el estado
        proveedores = Proveedor.objects.filter(Estado=estado_filtrado)
        total_proveedores = proveedores.count()

        # Serializar los proveedores
        serializer = ProveedorSerializer(proveedores, many=True)

        # Retornar datos junto con el conteo
        data = {
            "total": total_proveedores,
            "proveedores": serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)

#
# from django.urls import path
# from .views import ProveedorApiView, ProveedorDetailApiView
# app_name = 'proveedor'
#
# urlpatterns = [
#     path('proveedores/', ProveedorApiView.as_view(), name='api_proveedor'),
#     path('<int:pk>/', ProveedorDetailApiView.as_view()),
# ]