from django.urls import path
from .views import VentaAPIView

app_name = 'venta'
urlpatterns = [
    path('', VentaAPIView.as_view(), name='ventas'),
]