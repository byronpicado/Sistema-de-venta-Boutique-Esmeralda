from django.contrib import admin
from .models import Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('Descripcion', 'Estado', 'FechaRegistro')
    search_fields = ('Descripcion', 'Estado')
    list_filter = ('Estado', 'FechaRegistro')
