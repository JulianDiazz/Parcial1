from django import forms
from .models import Organizador, Evento

class OrganizadorForm(forms.ModelForm):
    class Meta:
        model = Organizador
        fields = ['nombre']

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo', 'descripcion', 'fecha', 'organizador']

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        if 'Cancelado' in titulo:
            raise forms.ValidationError("El título del evento no puede contener la palabra 'Cancelado'.")
        return titulo