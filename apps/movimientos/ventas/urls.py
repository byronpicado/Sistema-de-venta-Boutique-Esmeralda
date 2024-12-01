from django.urls import path
from .views import VentaAPIView, CancelarVentaView, ReporteVentaPorIDAPIView

urlpatterns = [
    path('', VentaAPIView.as_view(), name='venta'),
    path('ventas/cancelar/<int:pk>/', CancelarVentaView.as_view(), name='cancelar_venta'),
    path('ventas/<int:venta_id>/reporte/', ReporteVentaPorIDAPIView.as_view(), name='reporte-venta')
]
