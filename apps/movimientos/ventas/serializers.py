from rest_framework import serializers
from .models import DetalleVenta, Venta

"""
    Serializador de la clase DetalleVenta
"""


class DetalleVentaSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.CharField(source='producto.nombre', read_only=True)
    precio = serializers.DecimalField(source='producto.precio', read_only=True, max_digits=10, decimal_places=2)  # Añadir precio del producto con los parámetros necesarios

    class Meta:
        model = DetalleVenta
        fields = ['producto', 'cantidad', 'producto_nombre', 'precio']  # Incluye 'precio' en los campos
"""
    Serializador de la clase Venta
"""


from rest_framework import serializers
from .models import Venta

class VentaSerializer(serializers.ModelSerializer):
    total = serializers.DecimalField(read_only=True, max_digits=10, decimal_places=2)  # Definir max_digits y decimal_places

    class Meta:
        model = Venta
        fields = ['id', 'cliente', 'fecha', 'total']  # Asegúrate de incluir 'total' en los campos



"""
    Serializador de estadísticas de ventas
"""


class VentaEstadisticasSerializer(serializers.Serializer):
    total_ventas = serializers.IntegerField()
    total_ingresos = serializers.DecimalField(max_digits=12, decimal_places=2)

    ventas_por_mes = serializers.ListField(
        child=serializers.DictField(
            child=serializers.CharField()  # Define un solo tipo de valor si no es necesario validar más
        )
    )
    productos_populares = serializers.ListField(
        child=serializers.DictField(
            child=serializers.CharField()
        )
    )
    clientes_top = serializers.ListField(
        child=serializers.DictField(
            child=serializers.CharField()
        )
    )
