from django.db import models

# Create your models here.

class Pokemon(models.Model):
    id_pokemon  = models.IntegerField(verbose_name="Id pokemon")
    nombre      = models.CharField(verbose_name="Nombre", max_length=50, default="Sin nombre")
    #elemento    = models.CharField(verbose_name="Nombre", max_length=50, default="Sin nombre")
    vida        = models.IntegerField(verbose_name="Vida", default=100)
    energia     = models.DecimalField(verbose_name="Energía", decimal_places=4, max_digits=10, default=50.0)
    nivel       = models.IntegerField(verbose_name="Nivel", default=1)
    ivs         = models.IntegerField(verbose_name="Ivs", default=50)
    disponible  = models.BooleanField(verbose_name="Disponible", default=True)
    region      = models.CharField(verbose_name="Región", max_length=60, default="No definida")
    creado      = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)
    modificado  = models.DateTimeField(verbose_name="Fecha de modificación", auto_now=True)

    class Meta:
        verbose_name = 'Pokemon'
        verbose_name_plural = "Pokemon's"
        ordering = ['id_pokemon']


class Sensor(models.Model):
    temperatura = models.DecimalField(verbose_name="Temperatura", decimal_places=4, max_digits=10, default=50.0)
    humedad     = models.DecimalField(verbose_name="Humedad", decimal_places=4, max_digits=10, default=50.0)
    creado      = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)
    modificado  = models.DateTimeField(verbose_name="Fecha de modificación", auto_now=True)

    class Meta:
        verbose_name = 'Sensor'
        verbose_name_plural = "Sensores"
        ordering = ['id']
        