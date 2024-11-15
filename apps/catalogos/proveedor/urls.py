from django.urls import path
from .views import ProveedorApiView,ProveedorDetailApiView
app_name = 'proveedor'

urlpatterns = [
    path('proveedor/', ProveedorApiView.as_view(), name='api_proveedor'),
    path('<int:pk>/', ProveedorDetailApiView.as_view()),
]
