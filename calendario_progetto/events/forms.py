from django import forms
from .models import Evento

#crea automaticamente il form per l'evento
class EventoForm(forms.ModelForm):
    # fornisce i campi del form dalla classe Evento
    class Meta:
        model = Evento
        fields = ['titolo', 'descrizione', 'data', 'ora', 'categoria']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'ora': forms.TimeInput(attrs={'type': 'time'}),
        }