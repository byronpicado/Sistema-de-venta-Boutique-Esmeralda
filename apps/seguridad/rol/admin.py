from django.contrib import admin
from .models import Rol

@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ('Descripcion', 'FechaRegistro')
    search_fields = ('Descripcion',)
    list_filter = ('FechaRegistro',)
