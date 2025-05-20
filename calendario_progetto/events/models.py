from django.db import models
# non è necessario importare User se non lo usiamo
#from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class Evento(models.Model):
    #opzioni predefinite per l'evento
    titolo = models.CharField(max_length=100)
    descrizione = models.TextField(max_length=100, help_text="(max 100 caratteri)")
    data = models.DateField()
    ora = models.TimeField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.titolo}"