from datetime import timedelta, timezone
import logging

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema, logger
from django.shortcuts import get_object_or_404

from .models import Cliente
from .serializers import ClienteSerializer
from ...seguridad.permissions import CustomPermission


class ClienteApiView(APIView):
    @swagger_auto_schema(responses={200: ClienteSerializer(many=True)})
    def get(self, request):
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ClienteSerializer, responses={201: ClienteSerializer})
    def post(self, request):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClienteDetailApiView(APIView):
    @swagger_auto_schema(responses={200: ClienteSerializer})
    def get(self, request, pk=None):
        cliente = get_object_or_404(Cliente, pk=pk)
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ClienteSerializer, responses={200: ClienteSerializer})
    def put(self, request, pk):
        cliente = get_object_or_404(Cliente, pk=pk)
        serializer = ClienteSerializer(instance=cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=ClienteSerializer, responses={200: ClienteSerializer})
    def patch(self, request, pk):
        cliente = get_object_or_404(Cliente, pk=pk)
        serializer = ClienteSerializer(instance=cliente, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'Cliente eliminado correctamente'})
    def delete(self, request, pk):
        cliente = get_object_or_404(Cliente, pk=pk)
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # Obtiene el total de clientes activos.
    #
    # Esta función recupera el recuento total de clientes cuyo campo 'Estado' está establecido en True.
    # Devuelve una respuesta JSON que contiene un mensaje de éxito y el recuento total de clientes activos.
    #
class ClienteEstadisticasApiView(APIView):
    # permission_classes = [IsAuthenticated, CustomPermission]  # Comentar esta línea
    def get(self, request):
        total_activos = Cliente.objects.filter(Estado=True).count()
        return Response(
            {
                "message": "Total de clientes activos recuperados exitosamente.",
                "total_activos": total_activos,
            },
            status=status.HTTP_200_OK,
        )

