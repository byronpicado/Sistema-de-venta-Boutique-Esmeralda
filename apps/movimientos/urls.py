from django.urls import path, include

urlpatterns = [

    path('ventas/', include('apps.movimientos.ventas.urls')),
    path('compras/', include('apps.movimientos.compras.urls')),
]