from django.db import models

from apps.catalogos.producto.models import Producto
from apps.movimientos.ventas.models import Venta


class Detalle_Venta(models.Model):
    venta = models.ForeignKey(Venta, verbose_name='Codigo Venta', on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, verbose_name='Producto', on_delete=models.PROTECT)
    PrecioVenta = models.FloatField()
    Cantidad = models.CharField(max_length=100)
    SubTotal = models.DecimalField(max_digits=10, decimal_places=2)
    FechaRegistro = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Detalles de Ventas'

