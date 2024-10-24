from django.db import models

from apps.catalogos.proveedor.models import Proveedor
from apps.seguridad.usuarios.models import User


class Compra(models.Model):
    usuario = models.ForeignKey(User, verbose_name='Usuario', on_delete=models.PROTECT)
    proveedor = models.ForeignKey(Proveedor, verbose_name='Proveedor', on_delete=models.PROTECT)
    TipoDocumento = models.CharField(max_length=100)
    NumeroDocumento= models.CharField(max_length=100)
    MontoTotal = models.DecimalField(max_digits=10, decimal_places=2)
    FechaRegistro=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Compras'

    def __str__(self):
        return (f"{self.NumeroDocumento}")