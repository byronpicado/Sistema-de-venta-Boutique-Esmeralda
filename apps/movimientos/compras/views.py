from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.db import transaction
from .serializers import CompraSerializer
from .models import Compra, User, DetalleCompra, Producto, Proveedor
from drf_yasg.utils import swagger_auto_schema

"""
    Endpoint de Compra
"""
class CompraAPIView(APIView):
    @swagger_auto_schema(request_body=CompraSerializer)
    def post(self, request):
        serializer = CompraSerializer(data=request.data)

        if serializer.is_valid():
            try:
                with transaction.atomic():
                    proveedor = get_object_or_404(Proveedor, id=serializer.validated_data.get('proveedor').id)
                    comprador = get_object_or_404(User, id=serializer.validated_data.get('usuarios').id)
                    detalles_data = serializer.validated_data.get('detalles')
                    compra = Compra.objects.create(proveedor=proveedor, compradores=comprador, total = 0)
                    total_compra = 0

                    for detalle_data in detalles_data:
                        cantidad = detalle_data['cantidad']
                        producto = get_object_or_404(Producto, id=detalle_data['producto'].id)

                        subtotal = producto.precio * cantidad
                        total_compra += subtotal

                        producto.stock += cantidad
                        producto.save()

                        DetalleCompra.objects.create(
                            compra=compra,
                            producto=producto,
                            cantidad=cantidad,
                            subtotal=subtotal
                        )
                    compra.total = total_compra
                    compra.save()

                    compra_serializer = CompraSerializer(compra)
                    return Response(compra_serializer.data, status=status.HTTP_201_CREATED)



            except Exception as e:
                Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response