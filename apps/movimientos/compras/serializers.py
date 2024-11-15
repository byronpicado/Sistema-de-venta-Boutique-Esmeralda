from rest_framework.serializers import ModelSerializer, CharField
from .models import DetalleCompra, Compra

"""
    Serializador de la clase DetalleCompra
"""
class DetalleCompraSerializer(ModelSerializer):
    producto_nombre = CharField(source='producto.nombre', read_only=True)

    class Meta:
        model = DetalleCompra
        fields = ['producto', 'cantidad', 'producto_nombre', 'subtotal']  # Asegúrate de que sea 'subtotal' y no 'Subtotal'

"""
    Serializador de la clase Compra
"""
class CompraSerializer(ModelSerializer):
    proveedor_nombre = CharField(source='proveedor.RazonSocial', read_only=True)
    usuario_nombre = CharField(source='usuario.nombres', read_only=True)  # Cambia de Comprador_nombre a usuario_nombre
    detalles = DetalleCompraSerializer(many=True)

    class Meta:
        model = Compra
        fields = ['proveedor', 'proveedor_nombre', 'usuario', 'usuario_nombre', 'detalles']  # Corrige los nombres
