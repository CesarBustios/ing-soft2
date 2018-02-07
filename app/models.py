# -*- coding: utf-8 -*-
import math
from django.db import models


PUNTAJE_MINIMO = 85
PUNTAJE_MAXIMO = 100


class Seleccion(models.Model):
    pais = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'selecciones'


class Jugador(models.Model):
    nombre = models.CharField(max_length=200)
    idpais = models.ForeignKey('Seleccion', on_delete=models.CASCADE)

    @property
    def puntaje(self):
        return random.randint(PUNTAJE_MINIMO, PUNTAJE_MAXIMO)

    class Meta:
        managed = True
        db_table = 'jugadores'
