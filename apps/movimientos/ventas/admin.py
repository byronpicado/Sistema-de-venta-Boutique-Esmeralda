from django.contrib import admin
from .models import Venta

@admin.register(Venta)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('usuario','TipoDocumento', 'NumeroDocumento', 'DocumentoCliente','NombreCliente','MontoPago','MontoCambio', 'MontoTotal')
    search_fields = ('Fecharegistro',)
    list_filter = ('Fecharegistro',)
