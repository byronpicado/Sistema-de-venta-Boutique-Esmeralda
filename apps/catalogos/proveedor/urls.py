from django.urls import path
from .views import ProveedorApiView,ProveedorDetailApiView
app_name = 'proveedor'

urlpatterns = [
    path('proveedor/', ProveedorApiView.as_view(), name='api_proveedor'),
    path('proveedor/<int:pk>/', ProveedorDetailApiView.as_view(), name='api_proveedor_detail'),
]