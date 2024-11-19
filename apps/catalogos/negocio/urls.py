from django.urls import path
from .views import NegocioApiView, NegocioDetailApiView

app_name = 'negocio'

urlpatterns = [
    path('negocio/', NegocioApiView.as_view(), name='api_negocio'),
    path('producto/<int:pk>/', NegocioDetailApiView.as_view(), name='api_Negocio_detail'),
]