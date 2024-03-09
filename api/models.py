from django.db import models

# Create your models here.

class DragonBallModel(models.Model):
    nome=models.CharField(verbose_name=("Nome"), max_length=100, blank= True, null=True),
    raca=models.CharField(verbose_name=('Raça'), max_length=50, blank=True, null=True),
    gender=models.CharField(verbose_name=('Genero'), max_length=50, blank=True, null=True),
    ki=models.CharField(verbose_name=('Ki'), max_length=4000, blank=True, null=True),
    maxki=models.CharField(verbose_name=("MaxKi"), max_length=4000, blank=True, null=True),
    description=models.TextField(verbose_name=("Descrição"), blank=True, null=True),
    afiliacao=models.CharField(verbose_name=('Afiliação'), max_length=250, blank=True, null=True),
    planetaorigin=models.CharField(verbose_name=('Planeta de origem'), max_length=300, blank=True, null=True),