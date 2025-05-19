# Calendario Eventi - Applicazione Web Django

Un'applicazione web per la gestione di eventi in un calendario, sviluppata con il framework Django. L'applicazione permette di visualizzare, aggiungere, modificare ed eliminare eventi organizzati in un calendario mensile interattivo.

![Logo Progetto](/calendario_progetto/events/static/events/img/agm_solutions.png)

## 📋 Caratteristiche

- **Visualizzazione Calendario Mensile**: Interfaccia intuitiva con vista mensile e navigazione tra i mesi
- **Gestione Completa Eventi**: Creazione, visualizzazione, modifica ed eliminazione di eventi
- **Categorizzazione**: Organizzazione degli eventi per categorie
- **Interfaccia Responsive**: Design compatibile con dispositivi mobili e desktop
- **Vista Tabellare**: Elenco completo degli eventi con ordinamento e ricerca integrati

## ⚙️ Installazione

1. Clona il repository
   ```bash
   git clone https://github.com/Jhonpur/calendario_new.git
   ```

2. Crea un ambiente virtuale e attivalo
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   cd calendario-progetto
   ```

3. Installa le dipendenze
   ```bash
   pip install -r requirements.txt
   ```

4. Esegui le migrazioni del database
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Crea un superuser (opzionale)
   ```bash
   python manage.py createsuperuser
   ```

6. Avvia il server di sviluppo
   ```bash
   python manage.py runserver
   ```

7. Apri il browser all'indirizzo `http://127.0.0.1:8000/`

## 🛠️ Tecnologie Utilizzate

### Backend
- **Django**: Framework Python per lo sviluppo web
- **SQLite**: Database predefinito

### Frontend
- **Bootstrap 5**: Framework CSS per l'interfaccia utente responsive
- **SweetAlert2**: Per notifiche e dialoghi di conferma personalizzati
- **DataTables**: Per tabelle interattive con funzionalità di ricerca e ordinamento
- **jQuery**: Libreria JavaScript per manipolazione DOM

## 🏗️ Struttura del Progetto

L'applicazione è strutturata secondo il pattern MVC (Model-View-Controller) di Django:

### Models
- `Categoria`: Modello per la categorizzazione degli eventi
- `Evento`: Modello principale con titolo, descrizione, data, ora e categoria

### Views
- `calendario_mensile`: Visualizza il calendario con gli eventi del mese
- `aggiungi_evento`: Gestisce la creazione di nuovi eventi
- `modifica_evento`: Permette la modifica degli eventi esistenti
- `elimina_evento`: Gestisce l'eliminazione degli eventi
- `lista_eventi`: Mostra una lista tabellare di tutti gli eventi

### Templates
- Layout base con navbar e footer
- Template specifici per ogni operazione CRUD
- Componenti riutilizzabili per la visualizzazione degli eventi

## 📱 Funzionalità

### Visualizzazione Calendario
- Navigazione intuitiva tra i mesi
- Visualizzazione immediata degli eventi nel giorno corrispondente
- Preview rapida dei dettagli evento al click

### Gestione Eventi
- Form intuitivi per l'inserimento e la modifica
- Validazione dei dati inseriti
- Conferma di eliminazione per prevenire cancellazioni accidentali

### Lista Eventi
- Tabella interattiva con tutti gli eventi
- Ricerca istantanea
- Ordinamento per titolo, data, categoria
- Accesso rapido alle operazioni di modifica/eliminazione

## 🖼️ Screenshot

![Calendario Mensile](/calendario_progetto/events/static/events/img/cal_img.png)
*Vista del calendario mensile con eventi*

## 👥 Contatti

Per domande e suggerimenti, non esitate a contattarmi:
- Email: [lorenzo.pourpour@agmsolutions.net](mailto:lorenzo.pourpour@agmsolutions.net)
- GitHub: [Jhonpur](https://github.com/username)

---

Sviluppato da Lorenzo Pourpour
