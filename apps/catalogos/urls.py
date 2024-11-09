from django.urls import path, include

urlpatterns = [
    path('categoria/', include('apps.catalogos.categoria.urls')),
    path('cliente/', include('apps.catalogos.cliente.urls')),
]