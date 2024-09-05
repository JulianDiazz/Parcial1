from django.urls import path
from .views import lista_eventos
from .views import crearevento

urlpatterns = [
    path('eventos/', lista_eventos, name='lista_eventos'),
      path('eventos/crear/', crearevento, name='crearevento'),
]