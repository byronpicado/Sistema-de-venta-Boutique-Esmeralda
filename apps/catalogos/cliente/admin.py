from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('Documento', 'NombreCompleto', 'Correo', 'Telefono', 'Estado', 'FechaRegistro')
    search_fields = ('Documento', 'NombreCompleto', 'Correo', 'Telefono')
    list_filter = ('Estado', 'FechaRegistro')
