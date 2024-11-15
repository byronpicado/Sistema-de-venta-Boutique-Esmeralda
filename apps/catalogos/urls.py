from django.urls import path, include

urlpatterns = [
    path('categoria/', include('apps.catalogos.categoria.urls')),
    path('cliente/', include('apps.catalogos.cliente.urls')),
    path('cliente/', include('apps.catalogos.negocio.urls')),
    path('cliente/', include('apps.catalogos.producto.urls')),
    path('cliente/', include('apps.catalogos.proveedor.urls')),
]