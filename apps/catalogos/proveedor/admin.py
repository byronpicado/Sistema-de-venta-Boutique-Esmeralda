from django.contrib import admin
from .models import Proveedor

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('Documento', 'RazonSocial', 'Correo', 'Telefono', 'Estado', 'FechaRegistro')
    search_fields = ('Documento', 'RazonSocial', 'Correo', 'Telefono')
    list_filter = ('Estado', 'FechaRegistro')
