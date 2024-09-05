from django.shortcuts import render
from .models import Evento

def lista_eventos(request):
    eventos = Evento.objects.select_related('organizador').all()
    return render(request, 'eventos/eventos.html', {'eventos': eventos})