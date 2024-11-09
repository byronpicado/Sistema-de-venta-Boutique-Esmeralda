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
    @swagger_auto_schema(request_body=VentaSerializer)
    def post(self, request):
        serializer = VentaSerializer(data=request.data)

        if serializer.is_valid():
            try:
                with transaction.atomic():
                    cliente = get_object_or_404(Cliente, id=serializer.validated_data.get('cliente').id)
                    vendedor = get_object_or_404(User, id=serializer.validated_data.get('usuarios').id)
                    detalles_data = serializer.validated_data.get('detalles')
                    venta = Venta.objects.create(cliente=cliente, vendedores=vendedor, total = 0)
                    total_venta = 0

                    for detalle_data in detalles_data:
                        cantidad = detalle_data['cantidad']
                        producto = get_object_or_404(Producto, id=detalle_data['producto'].id)

                        if producto.stock < cantidad:
                            return Response(
                                {"Error": f"Stock insuficiente para el producto: {producto.nombre}"},
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
                Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)