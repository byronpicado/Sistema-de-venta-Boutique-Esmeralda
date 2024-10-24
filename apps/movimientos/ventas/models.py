from django.db import models
from apps.seguridad.usuarios.models import User

class Venta(models.Model):
    usuario = models.ForeignKey(User, verbose_name='Usuario', on_delete=models.PROTECT)
    TipoDocumento = models.CharField(max_length=100)
    NumeroDocumento = models.IntegerField()
    DocumentoCliente = models.IntegerField()
    NombreCliente = models.CharField(max_length=100)
    MontoPago = models.DecimalField(max_digits=10, decimal_places=2)
    MontoCambio = models.DecimalField(max_digits=10, decimal_places=2)
    MontoTotal = models.DecimalField(max_digits=10, decimal_places=2)
    Fecharegistro = models.DateField()
    TipoPago = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Ventas'

    def __str__(self):
        return f"{self.NumeroDocumento}"
