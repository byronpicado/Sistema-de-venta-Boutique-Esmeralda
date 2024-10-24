from django.contrib import admin
from .models import Permiso

@admin.register(Permiso)
class PermisoAdmin(admin.ModelAdmin):
    list_display = ('rol','NombreMenu', 'FechaRegistro')
    search_fields = ('NombreMenu',)
    list_filter = ('FechaRegistro',)
