from django.urls import path
from .views import usuarios_list  # Asegúrate de que la vista está importada correctamente

urlpatterns = [
    path('categorias/', usuarios_list, name='usuarios'),  # Sin paréntesis
]
