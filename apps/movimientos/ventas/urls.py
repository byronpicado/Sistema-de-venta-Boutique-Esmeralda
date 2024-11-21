from django.urls import path
from .views import VentaAPIView, CancelarVentaView, ReporteVentasAPIView

urlpatterns = [
    path('', VentaAPIView.as_view(), name='venta'),
    path('ventas/cancelar/<int:pk>/', CancelarVentaView.as_view(), name='cancelar_venta'),
    path('ventas/reporteVentas/<int:pk>/', ReporteVentasAPIView.as_view(), name='cancelar_venta'),
]
