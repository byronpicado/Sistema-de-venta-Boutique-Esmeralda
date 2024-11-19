from django.urls import path
from .views import ProductoApiView,ProductoDetailApiView
app_name = 'producto'

urlpatterns = [
    path('producto/', ProductoApiView.as_view(), name='api_producto'),
    path('producto/<int:pk>/', ProductoDetailApiView.as_view(), name='api_producto_detail'),
]