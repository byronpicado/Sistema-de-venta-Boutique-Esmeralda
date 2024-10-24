from django.db import models
from apps.seguridad.rol.models import Rol

class Permiso(models.Model):
    rol = models.ForeignKey(Rol, verbose_name='Rol', on_delete=models.PROTECT)
    NombreMenu = models.CharField(max_length=100)
    FechaRegistro = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Permisos'

    def __str__(self):
        return f"{self.rol} - {self.NombreMenu}"
