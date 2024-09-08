from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    lista_eventos,
    crear_evento,
    OrganizadorListView,
    OrganizadorCreateView,
    EventoUpdateView,
)

urlpatterns = [
    path('', lista_eventos, name='lista_eventos'),
    path('crear/', crear_evento, name='crear_evento'),
    path('organizadores/', OrganizadorListView.as_view(), name='organizador_list'),
    path('organizadores/crear/', OrganizadorCreateView.as_view(), name='organizador_create'),
    path('eventos/<int:pk>/editar/', EventoUpdateView.as_view(), name='editar_evento'),  
    path('login/', auth_views.LoginView.as_view(), name='login'),
    
]