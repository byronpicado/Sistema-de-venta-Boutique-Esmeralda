from django.urls import path, include

from apps.movimientos.ventas.serializers import VentaEstadisticasSerializer

urlpatterns = [

    path("", include('apps.movimientos.ventas.urls')),
    path('compras/', include('apps.movimientos.compras.urls')),

]