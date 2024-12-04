from django.urls import path
from .views import ClienteApiView, ClienteDetailApiView, ClienteEstadisticasApiView  # Importa la vista correcta

urlpatterns = [
    path("clientes/", ClienteApiView.as_view(), name="cliente_list"),
    path("clientes/<int:pk>/", ClienteDetailApiView.as_view(), name="cliente_detail"),
    path("clienteestadistica/", ClienteEstadisticasApiView.as_view(), name="cliente_estadistica"),  # Corrige aquí
]
