from django.db import models

class Rol(models.Model):
    Descripcion = models.CharField(max_length=100)
    FechaRegistro = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Roles'

    def __str__(self):
        return f"{self.Descripcion}"
