from django.urls import path
from .views import CompraAPIView

app_name = 'compra'
urlpatterns = [
    path('', CompraAPIView.as_view(), name='compra'),
]