from django.contrib import admin
from .models import Negocio

@admin.register(Negocio)
class NegocioAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'RUC', 'Direccion')
    search_fields = ('Nombre', 'RUC', 'Direccion')
