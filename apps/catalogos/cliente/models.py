from django.db import models

class Cliente(models.Model):
    Documento = models.CharField(max_length=100)
    NombreCompleto = models.CharField(max_length=100)
    Correo = models.CharField(max_length=100)
    Telefono = models.CharField(max_length=100)
    Estado = models.BooleanField(default=False)
    FechaRegistro = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return (f"{self.Documento} - {self.NombreCompleto}")
