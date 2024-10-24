from django.db import models

class Proveedor(models.Model):
    Documento = models.IntegerField()
    RazonSocial = models.CharField(max_length=100)
    Correo = models.CharField(max_length=100)
    Telefono = models.CharField(max_length=100)
    Estado = models.BooleanField(default=True)
    FechaRegistro = models.DateTimeField()


    class Meta:
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return (f"{self.Documento} - {self.RazonSocial}")