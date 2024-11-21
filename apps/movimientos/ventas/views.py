from django.http import JsonResponse
from django.shortcuts import get_object_or_404
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


from django.db.models import Sum

class ReporteVentasAPIView(APIView):
    """
    Genera un reporte de ventas.

    Método GET que permite generar un reporte de ventas filtrado por un rango de fechas.
    El reporte incluye la fecha, el total de ventas y la cantidad de productos vendidos.

    Parámetros:
    request (Request): La petición HTTP que contiene los parámetros de consulta.
        - fecha_inicio (str): Fecha de inicio del rango de fechas para filtrar las ventas.
        - fecha_fin (str): Fecha de fin del rango de fechas para filtrar las ventas.

    Retorna:
    Response: Un objeto de respuesta con el reporte de ventas o un mensaje de error.
        - status: Código de estado HTTP (200 OK si la operación es exitosa).
        - data: Lista de diccionarios que contienen la fecha, el total de ventas y la cantidad de productos vendidos.
    """

    def get(self, request):
        fecha_inicio = request.query_params.get('fecha_inicio')
        fecha_fin = request.query_params.get('fecha_fin')

        # Filtrar ventas por rango de fechas (opcional)
        ventas = Venta.objects.all()
        if fecha_inicio and fecha_fin:
            ventas = ventas.filter(fecha__range=[fecha_inicio, fecha_fin])

        # Agregar total de ventas y productos vendidos
        reporte = ventas.values('fecha__date').annotate(
            total_ventas=Sum('total'),
            cantidad_productos=Sum('detalles__cantidad')
        ).order_by('fecha__date')

        return Response(reporte, status=status.HTTP_200_OK)

