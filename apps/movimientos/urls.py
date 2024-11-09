from django.urls import path, include

urlpatterns = [

    path('ventas/', include('apps.movimientos.ventas.urls')),
]