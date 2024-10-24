from django.db import models

class Negocio(models.Model):
    Nombre = models.CharField(max_length=100)
    RUC = models.CharField(max_length=100)
    Direccion = models.CharField(max_length=100)
    Logo = models.ImageField(upload_to='logos/')

    class Meta:
        verbose_name_plural = 'Negocios'

    def __str__(self):
        return f"{self.Nombre} - {self.RUC}"
