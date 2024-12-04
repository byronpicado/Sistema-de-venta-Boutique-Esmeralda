from rest_framework import serializers  # Solo importa el serializers de DRF
from .models import Producto  # Importar el modelo Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('Codigo', 'Nombre', 'Descripcion', 'Stock', 'PrecioCompra', 'PrecioVenta', 'Estado', 'FechaRegistro')


class ProductoEstadisticasSerializer(serializers.Serializer):
    total_activos = serializers.IntegerField(read_only=True)
    total_stock = serializers.IntegerField(read_only=True)
    productos_por_categoria = serializers.DictField(child=serializers.IntegerField(), read_only=True)
