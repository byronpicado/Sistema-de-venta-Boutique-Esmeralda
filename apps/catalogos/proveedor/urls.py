from django.urls import path
from .views import ProveedorApiView, ProveedorDetailApiView, ProveedorEstadoApiView

app_name = 'proveedor'

urlpatterns = [
    path('proveedores/', ProveedorApiView.as_view(), name='api_proveedor'),
    path('proveedores/<int:pk>/', ProveedorDetailApiView.as_view(), name='api_proveedor_detail'),
    path('proveedores/estado/<str:estado>/', ProveedorEstadoApiView.as_view(), name='api_proveedor_estado'),
]
