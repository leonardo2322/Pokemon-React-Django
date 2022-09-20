from distutils.command.upload import upload
from django.db import models

# Create your models here.
class PokemonsBBDD(models.Model):
    nombre = models.CharField(max_length=200)
    categoria = models.CharField(max_length=200)
    habilidades = models.IntegerField()
    dano = models.IntegerField()
    img = models.ImageField(upload_to="images")