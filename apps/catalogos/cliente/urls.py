from django.urls import path
from .views import ClienteApiView, ClienteDetailApiView
app_name = 'cliente'

urlpatterns = [
    path('categorias/', ClienteApiView.as_view(), name='api_cliente'),
    path('<int:pk>/', ClienteDetailApiView.as_view()),
]
