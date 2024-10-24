from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('categoria','Codigo', 'Nombre', 'Descripcion', 'Stock', 'PrecioCompra',
                    'PrecioVenta', 'Estado', 'FechaRegistro')
    search_fields = ('Codigo', 'Nombre', 'Descripcion')
    list_filter = ('Estado', 'FechaRegistro')

    def nombreCategoria(self, obj):
        return obj.Categoria.Descripcion