from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from apps.seguridad.usuarios.models import User

@admin.register(User)
class UserAdmin(UserAdmin):
    pass
