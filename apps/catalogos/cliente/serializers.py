from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('Documento', 'NombreCompleto', 'Correo', 'Telefono', 'Estado', 'FechaRegistro')


class ClienteEstadisticasSerializer(serializers.Serializer):
    total_activos = serializers.IntegerField(read_only=True)