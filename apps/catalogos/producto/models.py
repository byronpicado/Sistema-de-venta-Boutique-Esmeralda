from django.db import models
from apps.catalogos.categoria.models import Categoria

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, verbose_name='Categoria', on_delete=models.PROTECT)

    Codigo=models.CharField(max_length=50)
    Nombre=models.CharField(max_length=50)
    Descripcion=models.CharField(max_length=50)
    Stock=models.IntegerField()
    PrecioCompra=models.DecimalField(max_digits=10,decimal_places=2)
    PrecioVenta=models.DecimalField(max_digits=10,decimal_places=2)
    Estado =models.BooleanField(default=False)
    FechaRegistro = models.DateTimeField()


    class Meta:
        verbose_name_plural = 'Productos'

    def __str__(self):
        return f"{self.Nombre} - Stock: {self.Stock}"


