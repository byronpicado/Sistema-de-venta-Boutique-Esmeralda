from django.db import models
from apps.catalogos.producto.models import Producto
from apps.movimientos.compras.models import Compra


class Detalle_Compra(models.Model):
    compra = models.ForeignKey(Compra, verbose_name='Codigo Compra', on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, verbose_name='Producto', on_delete=models.PROTECT)
    PrecioCompra = models.DecimalField(max_digits=10, decimal_places=2)
    PrecioVenta = models.DecimalField(decimal_places=2, max_digits=10)  # Adjusted max_digits for consistency
    Cantidad = models.IntegerField()
    FechaRegistro = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Detalles de Compras'

