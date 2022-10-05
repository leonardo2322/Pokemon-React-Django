from email.policy import default
from django.db import models
from django.utils.translation import gettext_lazy as _


def upload_to(instance,filename):
    return "images/{filename}".format(filename=filename)
# Create your models here.
class PokemonsBBDD(models.Model):
    nombre = models.CharField(max_length=200)
    categoria = models.CharField(max_length=200)
    habilidades = models.CharField(max_length=250)
    dano = models.IntegerField()
    img = models.ImageField(_("images"),upload_to=upload_to,blank=True,null=True,default='images/squirtle.png')
    
    def __str__(self):
        return self.nombre