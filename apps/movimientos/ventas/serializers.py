from rest_framework.serializers import ModelSerializer, CharField
from .models import  DetalleVenta, Venta

"""
    Serializador de la clase DetalleVenta
"""
class DetalleVentaSerializer(ModelSerializer):
    producto_nombre = CharField(source='producto.nombre', read_only=True)
    class Meta:
        model = DetalleVenta
        fields = ['producto', 'cantidad', 'producto_nombre']

"""
    Serializador de la clase Venta
"""
class VentaSerializer(ModelSerializer):
    cliente_nombre = CharField(source='cliente.nombres', read_only=True)
    vendedor_nombre = CharField(source='vendedores.nombres', read_only=True)
    detalles = DetalleVentaSerializer(many=True)

    class Meta:
        model = Venta
        fields = ['cliente', 'cliente_nombre', 'vendedores', 'vendedor_nombre', 'detalles']