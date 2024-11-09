from django.urls import path
from .views import CategoriaApiView, CategoriaDetailApiView
app_name = 'categoria'

urlpatterns = [
    path('categorias/', CategoriaApiView.as_view(), name='api_categoria'),
    path('<int:pk>/', CategoriaDetailApiView.as_view()),
]
