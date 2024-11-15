from rest_framework.serializers import ModelSerializer
from .models import Producto  # Importar el modelo Producto

class ProductoSerializer(ModelSerializer):
    class Meta:
        model = Producto  # Usa el modelo Producto aquí
        fields = ('Codigo', 'Nombre', 'Descripcion', 'Stock', 'PrecioCompra', 'PrecioVenta', 'Estado', 'FechaRegistro')
