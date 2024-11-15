from rest_framework.serializers import ModelSerializer
from .models import Proveedor

class ProveedorSerializer(ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ('Documento', 'RazonSocial', 'Correo', 'Telefono', 'Estado', 'FechaRegistro')