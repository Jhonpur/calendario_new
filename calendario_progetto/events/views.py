from django.shortcuts import render, redirect, get_object_or_404
#from django.contrib.auth.decorators import login_required
from .models import Evento, Categoria
from .forms import EventoForm
import calendar
from datetime import datetime, timedelta

# Create your views here.
def calendario_mensile(request):
    # Ottengo il mese e l'anno corrente
    anno = datetime.now().year
    mese = datetime.now().month
    # Ottengo il mese e l'anno dalla richiesta GET, se presenti
    anno = request.GET.get('anno', anno)
    mese = request.GET.get('mese', mese)

    anno = int(anno)
    mese = int(mese)
    
    #calcolo mese e anno precedenti e successivi
    mese_prec = mese - 1
    anno_prec = anno
    if mese_prec == 0:
        mese_prec = 12
        anno_prec -= 1
        
    mese_succ = mese + 1
    anno_succ = anno
    if mese_succ == 13:
        mese_succ = 1
        anno_succ += 1

     # Ottengo il nome del mese in italiano
    nomi_mesi = ['', 'Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio', 'Giugno', 
                'Luglio', 'Agosto', 'Settembre', 'Ottobre', 'Novembre', 'Dicembre']
    # Ottengo il nome del mese corrente al posto del numero
    nome_mese = nomi_mesi[mese]

    #calendario creato
    cal = calendar.monthcalendar(anno, mese)

    primi_del_mese = datetime(anno, mese, 1)
    ultimo_del_mese = datetime(anno, mese, calendar.monthrange(anno, mese)[1])

    # Ottengo gli eventi in base alla data, filtrando per il mese e l'anno selezionati
    eventi = Evento.objects.filter(
        data__range = [primi_del_mese, ultimo_del_mese]
    )

    context = {
        'calendario': cal,
        'anno': anno,
        'mese': mese,
        'nome_mese': nome_mese,
        'eventi': eventi,
        'anno_prec': anno_prec,
        'mese_prec': mese_prec,
        'anno_succ': anno_succ,
        'mese_succ': mese_succ,
    }
    return render(request, 'events/calendario_mensile.html', context)


def aggiungi_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendario_mensile')
    else:
        form = EventoForm()
    return render(request, 'events/aggiungi_evento.html', {'form': form})


def modifica_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('calendario_mensile')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'events/modifica_evento.html', {'form': form, 'evento': evento})


def elimina_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    if request.method == 'POST':
        evento.delete()
        return redirect('calendario_mensile')
    return render(request, 'events/elimina_evento.html', {'evento': evento})


def lista_eventi(request):
    eventi = Evento.objects.all()
    return render(request, 'events/lista_eventi.html', {'eventi': eventi})