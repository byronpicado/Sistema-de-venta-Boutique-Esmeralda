from django.db import models

class Categoria(models.Model):
    Descripcion = models.CharField(max_length=100)
    Estado = models.BooleanField(default=True)
    FechaRegistro  = models.DateTimeField('Fecha de registro')

    class Meta:
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return f"{self.Descripcion}"