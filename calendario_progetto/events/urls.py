from django.urls import path
from . import views


urlpatterns = [
    path('', views.calendario_mensile, name='calendario_mensile'),
    path('aggiungi/', views.aggiungi_evento, name='aggiungi_evento'),
    path('modifica/<int:evento_id>/', views.modifica_evento, name='modifica_evento'),
    path('elimina/<int:evento_id>/', views.elimina_evento, name='elimina_evento'),
    path('eventi/', views.lista_eventi, name='lista_eventi'),
]