from django.db import models
from apps.catalogos.producto.models import Producto
from apps.catalogos.proveedor.models import Proveedor
from apps.seguridad.usuarios.models import User

class Compra(models.Model):
    usuario = models.ForeignKey(User, verbose_name='Usuario', on_delete=models.PROTECT)
    proveedor = models.ForeignKey(Proveedor, verbose_name='Proveedor', on_delete=models.PROTECT)
    TipoDocumento = models.CharField(max_length=100)
    NumeroDocumento= models.CharField(max_length=100)
    MontoTotal = models.DecimalField(max_digits=10, decimal_places=2)
    FechaRegistro=models.DateField(auto_now_add=True)

class DetalleCompra(models.Model):
        compra = models.ForeignKey(Compra, related_name='detalles', on_delete=models.PROTECT)
        producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
        cantidad = models.IntegerField()
        subtotal = models.DecimalField(max_digits=10, decimal_places=2)