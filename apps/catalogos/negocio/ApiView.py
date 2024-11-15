from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Negocio  # Asegúrate de tener el modelo Negocio importado
from .serializers import NegocioSerializer  # Asegúrate de tener el serializador NegocioSerializer importado
from drf_yasg.utils import swagger_auto_schema

class NegocioApiView(APIView):

    @swagger_auto_schema(responses={200: NegocioSerializer(many=True)})
    def get(self, request):
        negocios = Negocio.objects.all()  # Obtiene todos los negocios
        serializer = NegocioSerializer(negocios, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=NegocioSerializer, responses={200: NegocioSerializer})
    def post(self, request):
        serializer = NegocioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NegocioDetailApiView(APIView):

    @swagger_auto_schema(responses={200: NegocioSerializer})
    def get(self, request, pk):
        try:
            negocio = Negocio.objects.get(pk=pk)
        except Negocio.DoesNotExist:
            return Response({'error': 'Negocio no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = NegocioSerializer(negocio)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=NegocioSerializer, responses={200: NegocioSerializer})
    def put(self, request, pk):
        try:
            negocio = Negocio.objects.get(pk=pk)
        except Negocio.DoesNotExist:
            return Response({'error': 'Negocio no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = NegocioSerializer(instance=negocio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=NegocioSerializer, responses={200: NegocioSerializer})
    def patch(self, request, pk):
        try:
            negocio = Negocio.objects.get(pk=pk)
        except Negocio.DoesNotExist:
            return Response({'error': 'Negocio no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = NegocioSerializer(instance=negocio, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'Negocio eliminado correctamente'})
    def delete(self, request, pk):
        try:
            negocio = Negocio.objects.get(pk=pk)
        except Negocio.DoesNotExist:
            return Response({'error': 'Negocio no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        try:
            negocio.delete()
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(status=status.HTTP_204_NO_CONTENT)

