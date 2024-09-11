from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.utils.decorators import method_decorator
from .models import Evento, Organizador
from .forms import EventoForm, OrganizadorForm

@login_required
def lista_eventos(request):
    eventos = Evento.objects.all().select_related('organizador')
    return render(request, 'eventos/lista_eventos.html', {'eventos': eventos})

@login_required
def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = EventoForm()
    return render(request, 'eventos/crear_evento.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class OrganizadorListView(ListView):
    model = Organizador
    template_name = 'eventos/lista_organizadores.html'
    context_object_name = 'organizadores'

@method_decorator(login_required, name='dispatch')
class OrganizadorCreateView(CreateView):
    model = Organizador
    form_class = OrganizadorForm
    template_name = 'eventos/organizador_form.html'
    success_url = reverse_lazy('organizador_list')

@method_decorator(login_required, name='dispatch')
class EventoUpdateView(UpdateView):
    model = Evento
    form_class = EventoForm
    template_name = 'eventos/editar_evento.html'
    success_url = reverse_lazy('lista_eventos')


class MyLoginView(LoginView):
    template_name = 'eventos/login.html'
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('lista_eventos')  
        return super().get(request, *args, **kwargs)