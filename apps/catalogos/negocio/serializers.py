from rest_framework.serializers import ModelSerializer
from .models import Negocio

class NegocioSerializer(ModelSerializer):
    class Meta:
        model = Negocio
        fields = ('Nombre', 'RUC', 'Direccion', 'Logo')