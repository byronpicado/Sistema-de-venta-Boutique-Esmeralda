from django.urls import path
from .views import VentaAPIView, VentaEstadisticaAPIView

urlpatterns = [
    # Ruta para obtener y crear ventas
    path('ventas/', VentaAPIView.as_view(), name='venta'),

    # Ruta para obtener estadísticas de ventas
    path("ventas/estadistica/", VentaEstadisticaAPIView.as_view(), name="estadisticas"),

    # Ruta para actualizar o eliminar una venta específica
    path('ventas/<int:pk>/', VentaAPIView.as_view(), name='venta-detalle'),
]
