from datetime import timezone

from django.db import models
from apps.catalogos.cliente.models import Cliente
from apps.seguridad.usuarios.models import User
from apps.catalogos.producto.models import Producto

class Venta(models.Model):
    """
    This class represents a Venta in the SistemaBoutiqueEsmeralda application.

    Attributes:
    - cliente: The related Cliente object.
    - vendedores: The related User object representing the seller.
    - fecha: The date and time of the sale.
    - total: The total amount of the sale.
    - estado: The current state of the sale.
    """

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
        """
        Cancels the sale if it's not already cancelled.

        If the sale is not cancelled, it changes the state to 'CANCELADA', saves the changes,
        and reverts the inventory changes made during the sale.
        """
        if self.estado != 'CANCELADA':
            self.estado = 'CANCELADA'
            self.save()
            self._ajustar_inventario()

    def _ajustar_inventario(self):
        """
        Reverts inventory changes made during the sale if the sale is cancelled.

        Iterates through all the related DetalleVenta objects and increases the stock of the
        corresponding Producto objects by the quantity sold in the cancelled sale.
        """
        for detalle in self.detalles.all():
            detalle.producto.stock += detalle.cantidad
            detalle.producto.save()

    def __str__(self):
        """
        Returns a string representation of the Venta object.

        The string representation includes the sale ID, client, total amount, and state.
        """
        return f"Venta {self.id} - {self.cliente} - {self.total} ({self.estado})"


class DetalleVenta(models.Model):
    """
    This class represents a DetalleVenta in the SistemaBoutiqueEsmeralda application.
    A DetalleVenta is a part of a Venta and contains information about a specific product sold.

    Attributes:
    - venta: The related Venta object.
    - producto: The related Producto object.
    - cantidad: The quantity of the product sold.
    - subtotal: The subtotal of the product sold (quantity * price).
    """

    venta = models.ForeignKey(Venta, related_name='detalles', on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)