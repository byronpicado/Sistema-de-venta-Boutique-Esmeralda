from mmap import error

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from yaml import serialize

from apps.catalogos.categoria.models import Categoria
from .serializers import CategoriaSerializer
from drf_yasg.utils import swagger_auto_schema

class CategoriaApiView(APIView):

    @swagger_auto_schema(responses={200: CategoriaSerializer(many=True)})
    def get(self, request):

     categorias = Categoria.objects.all()
     serializer = CategoriaSerializer(categorias, many=True)
     return Response(serializer.data)

    @swagger_auto_schema(request_body=CategoriaSerializer, responses={200: CategoriaSerializer})
    def post(self, request):
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoriaDetailApiView(APIView):

    @swagger_auto_schema(responses={200: CategoriaSerializer})
    def get(self, request, pk:None):
        try:
            categoria = Categoria.objects.get(pk=pk)
        except Categoria.DoesNotExist:
            return Response({'error': 'Categoria no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CategoriaSerializer, responses={200: CategoriaSerializer})
    def put(self, request, pk):
        try:
            categoria = Categoria.objects.get(pk=pk)
        except Categoria.DoesNotExist:  # Corregido aquí
            return Response({'error': 'Categoria no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CategoriaSerializer(instance=categoria,
                                         data=request.data)  # Corregí el typo "serialazer" por "serializer"
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=CategoriaSerializer, responses={200: CategoriaSerializer})
    def patch(self, request, pk):
        try:
            categoria = Categoria.objects.get(pk=pk)
        except Categoria.DoesNotExist:
            return Response({'error': 'Categoria no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serialazer = CategoriaSerializer(instance=categoria, data=request.data, partial=True)
        if serialazer.is_valid():
            serialazer.save()
            return Response(serialazer.data)
        return Response(serialazer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'Categoría eliminada correctamente'})

    def delete(self, request, pk):
        try:
            categoria = Categoria.objects.get(pk=pk)
        except Categoria.DoesNotExist:
            return Response({'error': 'Categoria no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        try:
            categoria.delete()
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(status=status.HTTP_204_NO_CONTENT)

#
# from django.urls import path
# from .views import CategoriaApiView, CategoriaDetailApiView
# app_name = 'categoria'
#
# urlpatterns = [
#     path('categorias/', CategoriaApiView.as_view(), name='api_categoria'),
#     path('<int:pk>/', CategoriaDetailApiView.as_view()),
# ]
