from datetime import timezone

from django.db import models
from apps.catalogos.cliente.models import Cliente
from apps.seguridad.usuarios.models import User
from apps.catalogos.producto.models import Producto
from django.db.models import F, Sum


class Venta(models.Model):
    ESTADO_CHOICES = [
        ('ACTIVA', 'Activa'),
        ('CANCELADA', 'Cancelada'),
    ]
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    vendedores = models.ForeignKey(User, on_delete=models.PROTECT)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='ACTIVA')
    fecha_cancelacion = models.DateTimeField(null=True, blank=True)

    def calcular_total(self):
        # Calcula el total de la venta sumando los subtotales de los detalles.
        return self.detalles.aggregate(total=Sum(F('subtotal')))['total'] or 0

    def save(self, *args, **kwargs):
        if not self.pk:  # Si es una nueva venta, calcula el total al guardar.
            self.total = self.calcular_total()
        super().save(*args, **kwargs)

    def cancelada(self):
        self.estado = 'CANCELADA'
        self.fecha_cancelacion = timezone.now()
        self.save()

    def __str__(self):
        return f"Venta {self.id} - {self.cliente.nombrecompleto}"


class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, related_name='detalles', on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def calcular_subtotal(self):
        # Calcula el subtotal como cantidad * precio del producto
        self.subtotal = self.cantidad * self.producto.precio
        return self.subtotal

    def save(self, *args, **kwargs):
        self.calcular_subtotal()  # Calcula el subtotal antes de guardar
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Detalle Venta {self.id} - Producto {self.producto.nombre}"

