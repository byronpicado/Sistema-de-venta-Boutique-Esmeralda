from django.db import transaction
from django.db.models import Sum, Count, F
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
import logging
import datetime

from .models import Venta, DetalleVenta, Producto, Cliente
from .serializers import VentaSerializer, VentaEstadisticasSerializer, DetalleVentaSerializer

# Configura el logger
logger = logging.getLogger(__name__)

class VentaAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: VentaSerializer(many=True)})
    def get(self, request):
        """
        Obtiene todas las ventas activas (no eliminadas).
        """
        ventas = Venta.objects.filter(isdeleted=False)
        serializer = VentaSerializer(ventas, many=True)
        logger.info(f"El usuario '{request.user}' recuperó {ventas.count()} ventas.")
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=VentaSerializer)
    def post(self, request):
        """
        Crea una nueva venta con sus detalles.
        """
        serializer = VentaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            with transaction.atomic():
                # Guarda la venta principal
                venta = serializer.save()

                # Guarda los detalles de la venta
                for detalle_data in request.data.get('detalles', []):
                    detalle_serializer = DetalleVentaSerializer(data=detalle_data)
                    detalle_serializer.is_valid(raise_exception=True)
                    detalle_serializer.save(venta=venta)  # Relaciona el detalle con la venta

                logger.info(f"El usuario '{request.user}' creó una nueva venta con ID: {venta.id}.")
                return Response(
                    {"message": "La venta se creó exitosamente.", "data": serializer.data},
                    status=status.HTTP_201_CREATED
                )
        except Exception as e:
            logger.error(f"Error al crear la venta: {e}")
            return Response(
                {"error": "Hubo un error al crear la venta."}, status=status.HTTP_400_BAD_REQUEST
            )

    @swagger_auto_schema(request_body=VentaSerializer)
    def patch(self, request, pk):
        """
        Actualiza una venta específica.
        """
        venta = get_object_or_404(Venta, id=pk)
        serializer = VentaSerializer(venta, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        logger.info(f"El usuario '{request.user}' actualizó la venta con ID: {pk}.")
        return Response(
            {"message": "La venta se actualizó exitosamente.", "data": serializer.data},
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Elimina una venta de forma lógica.
        """
        venta = get_object_or_404(Venta, id=pk)
        venta.isdeleted = True
        venta.save()
        logger.info(f"El usuario '{request.user}' eliminó la venta con ID: {pk}.")
        return Response(
            {"message": f"La venta con ID {pk} fue eliminada de forma lógica."},
            status=status.HTTP_204_NO_CONTENT
        )


class VentaEstadisticaAPIView(APIView):
    """
    Genera estadísticas relacionadas con las ventas en el sistema.
    """

    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: VentaEstadisticasSerializer})
    def get(self, request):
        """
        Genera estadísticas sobre las ventas activas (no canceladas).
        """

        # Ventas activas
        ventas_activas = Venta.objects.filter(estado='ACTIVA')

        # Estadísticas generales
        total_ventas = ventas_activas.count()
        total_ingresos = ventas_activas.aggregate(ingresos_totales=Sum('monto_total'))['ingresos_totales'] or 0

        # Ventas por mes en el año actual
        mes_actual = datetime.datetime.now().year
        ventas_por_mes = (
            ventas_activas.filter(fecha__year=mes_actual)
            .annotate(mes=F('fecha__month'))
            .values('mes')
            .annotate(total=Sum('total'), cantidad=Count('id'))
            .order_by('mes')
        )

        # Productos más vendidos
        productos_populares = (
            DetalleVenta.objects.filter(venta__estado='ACTIVA')
            .values('producto__nombre')
            .annotate(total_cantidad=Sum('cantidad'))
            .order_by('-total_cantidad')[:5]
        )

        # Clientes con más compras
        clientes_top = (
            ventas_activas.values('cliente__nombre')
            .annotate(total_compras=Count('id'), monto_total=Sum('total'))
            .order_by('-monto_total')[:5]
        )

        # Construcción del reporte de estadísticas
        estadisticas = {
            "total_ventas": total_ventas,
            "total_ingresos": total_ingresos,
            "ventas_por_mes": list(ventas_por_mes),
            "productos_populares": list(productos_populares),
            "clientes_top": list(clientes_top),
        }

        serializer = VentaEstadisticasSerializer(estadisticas)
        return Response(serializer.data, status=status.HTTP_200_OK)

