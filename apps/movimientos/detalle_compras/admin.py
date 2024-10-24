from django.contrib import admin
from .models import Detalle_Compra

@admin.register(Detalle_Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('compra', 'producto', 'PrecioCompra', 'PrecioVenta', 'Cantidad', 'FechaRegistro')
    search_fields = ('compra_codigo', 'producto__nombre', 'FechaRegistro')
    list_filter = ('FechaRegistro',)
