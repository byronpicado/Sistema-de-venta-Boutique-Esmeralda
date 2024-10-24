from django.contrib import admin
from .models import Detalle_Venta

class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ('venta', 'producto', 'PrecioVenta', 'Cantidad', 'SubTotal', 'FechaRegistro')
    search_fields = ('IdVenta', 'IdProducto')
    list_filter = ('FechaRegistro',)
    ordering = ('-FechaRegistro',)  # Ordena por fecha de registro descendente
    readonly_fields = ('FechaRegistro',)  # Evita modificar este campo en el admin

admin.site.register(Detalle_Venta, DetalleVentaAdmin)
