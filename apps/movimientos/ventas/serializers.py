from rest_framework.serializers import ModelSerializer, CharField
from .models import  DetalleVenta, Venta

"""
    Serializador de la clase DetalleVenta
"""
class DetalleVentaSerializer(ModelSerializer):
    """
    Serializer for DetalleVenta model.

    This serializer is used to represent the details of a single sale item. It includes the product,
    its quantity, and the product's name.

    Attributes:
    - producto_nombre: A read-only field that represents the name of the product. It is derived from the 'nombre' attribute of the 'producto' field.
    """

    producto_nombre = CharField(source='producto.nombre', read_only=True)

    class Meta:
        """
        Metaclass for DetalleVentaSerializer.

        Defines the model and fields to be included in the serializer.
        """

        model = DetalleVenta
        fields = ['producto', 'cantidad', 'producto_nombre']

"""
    Serializador de la clase Venta
"""
class VentaSerializer(ModelSerializer):
    cliente_nombre = CharField(source='cliente.nombres', read_only=True)
    vendedor_nombre = CharField(source='usuarios.name', read_only=True)
    detalles = DetalleVentaSerializer(many=True)

    class Meta:
        model = Venta
        fields = ['cliente', 'cliente_nombre', 'vendedores', 'vendedor_nombre', 'detalles']