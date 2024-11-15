from django.urls import path
from .views import NegocioApiView, NegocioDetailApiView

app_name = 'negocio'

urlpatterns = [
    path('negocios/', NegocioApiView.as_view(), name='api_negocio'),  # Cambié 'categorias' por 'negocios'
    path('<int:pk>/', NegocioDetailApiView.as_view()),
]
