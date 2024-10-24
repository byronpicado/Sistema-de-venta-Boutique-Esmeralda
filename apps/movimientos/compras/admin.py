from django.contrib import admin
from .models import Compra

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('usuario','proveedor','TipoDocumento', 'NumeroDocumento', 'MontoTotal','FechaRegistro')
    search_fields = ('NumeroDocumento','FechaRegistro')
    list_filter = ('FechaRegistro',)
