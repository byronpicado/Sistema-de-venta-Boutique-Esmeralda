from datetime import timezone

from django.db import models
from apps.catalogos.cliente.models import Cliente
from apps.seguridad.usuarios.models import User
from apps.catalogos.producto.models import Producto

class Venta(models.Model):
    ESTADO_CHOICES = [
        ('ACTIVA', 'Activa'),
        ('CANCELADA', 'Cancelada'),
    ]
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    vendedores = models.ForeignKey(User, on_delete=models.PROTECT)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='ACTIVA')

    def cancelar(self):
        if self.estado != 'CANCELADA':
            self.estado = 'CANCELADA'
            self.save()
            self._ajustar_inventario()

    def _ajustar_inventario(self):
        """Revertir cambios en el inventario si la venta es cancelada."""
        for detalle in self.detalles.all():
            detalle.producto.stock += detalle.cantidad
            detalle.producto.save()

    def __str__(self):
        return f"Venta {self.id} - {self.cliente} - {self.total} ({self.estado})"


class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, related_name='detalles' , on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)