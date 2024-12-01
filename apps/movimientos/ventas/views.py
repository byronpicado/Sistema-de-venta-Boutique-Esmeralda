from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.db import transaction
from .serializers import VentaSerializer
from .models import Venta, User, DetalleVenta, Producto, Cliente
from drf_yasg.utils import swagger_auto_schema

"""
    Endpoint de Venta
"""
class VentaAPIView(APIView):
    """
    This class handles the creation of new sales in the system.

    Methods:
    post: Creates a new sale record in the database.
    """

    @swagger_auto_schema(request_body=VentaSerializer)
    def post(self, request):
        """
        Creates a new sale record in the database.

        Parameters:
        request (Request): The incoming request containing the sale data.

        Returns:
        Response: A response object with the created sale data or an error message.
        """
class VentaAPIView(APIView):
    """
    Maneja la creación de nuevas ventas en el sistema.
    """

    @swagger_auto_schema(request_body=VentaSerializer)
    def post(self, request):
        serializer = VentaSerializer(data=request.data)

        if serializer.is_valid():
            try:
                with transaction.atomic():
                    cliente = get_object_or_404(Cliente, id=serializer.validated_data.get('cliente').id)
                    vendedor = get_object_or_404(User, id=serializer.validated_data.get('usuarios').id)
                    detalles_data = serializer.validated_data.get('detalles')
                    venta = Venta.objects.create(cliente=cliente, vendedores=vendedor, total=0)
                    total_venta = 0

                    for detalle_data in detalles_data:
                        cantidad = detalle_data['cantidad']
                        producto = get_object_or_404(Producto, id=detalle_data['producto'].id)

                        if producto.stock < cantidad:
                            return Response(
                                {"error": f"Stock insuficiente para el producto: {producto.nombre}"},
                                status=status.HTTP_400_BAD_REQUEST
                            )

                        subtotal = producto.precio * cantidad
                        total_venta += subtotal

                        producto.stock -= cantidad
                        producto.save()

                        DetalleVenta.objects.create(
                            venta=venta,
                            producto=producto,
                            cantidad=cantidad,
                            subtotal=subtotal
                        )

                    venta.total = total_venta
                    venta.save()

                    venta_serializer = VentaSerializer(venta)
                    return Response(venta_serializer.data, status=status.HTTP_201_CREATED)

            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CancelarVentaView(APIView):
    """
    Cancels a sale in the system.

    This class handles the cancellation of a sale by its ID. It retrieves the sale from the database,
    calls the 'cancelar' method on the sale object, and returns a JSON response indicating the success
    or failure of the cancellation.

    Parameters:
    request (Request): The incoming HTTP request containing the sale ID to be canceled.
    venta_id (int): The ID of the sale to be canceled.

    Returns:
    JsonResponse: A JSON response indicating the success or failure of the cancellation.
        - If the sale is successfully canceled, the response contains a 'message' key with the value
          'Venta cancelada con éxito.'
        - If the sale is not found, the response contains an 'error' key with the value 'Venta no encontrada.'
          and a status code of 404.
        - If an error occurs during the cancellation process, the response contains an 'error' key with
          the error message and a status code of 400.
    """

    def post(self, request, venta_id):
        try:
            venta = Venta.objects.get(id=venta_id)
            venta.cancelar()
            return JsonResponse({'message': 'Venta cancelada con éxito.'})
        except Venta.DoesNotExist:
            return JsonResponse({'error': 'Venta no encontrada.'}, status=404)
        except ValueError as e:
            return JsonResponse({'error': str(e)}, status=400)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Venta

class ReporteVentaPorIDAPIView(APIView):
    """
    Genera un reporte de una venta específica dado su ID.
    """

    def get(self, request, venta_id):
        # Buscar la venta por ID
        venta = get_object_or_404(Venta, id=venta_id)

        # Obtener los detalles de la venta
        detalles = venta.detalleventa_set.all()  # Relación inversa desde el modelo DetalleVenta

        # Preparar los datos del reporte
        reporte = {
            "venta_id": venta.id,
            "total_venta": venta.total,
            "productos": [
                {
                    "producto_id": detalle.producto.id,
                    "nombre": detalle.producto.nombre,
                    "cantidad": detalle.cantidad,
                    "subtotal": detalle.subtotal
                }
                for detalle in detalles
            ]
        }

        # Retornar el reporte como respuesta JSON
        return Response(reporte, status=status.HTTP_200_OK)