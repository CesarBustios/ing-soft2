# -*- coding: utf-8 -*-
from django import forms


class EquipoForm(forms.Form):
    POSICION_CHOICES = (
        ('arquero', 'ARQUERO'),
        ('defensa1', 'DEFENSA 1'),
        ('defensa2', 'DEFENSA 2'),
        ('defensa3', 'DEFENSA 3'),
        ('defensa4', 'DEFENSA 4'),
        ('centro1', 'CENTRO 1'),
        ('centro2', 'CENTRO 2'),
        ('centro3', 'CENTRO 3'),
        ('delantero1', 'DELANTERO 1'),
        ('delantero2', 'DELANTERO 2'),
        ('delantero3', 'DELANTERO 3'),
    )
    posicion = forms.ChoiceField(choices=POSICION_CHOICES, widget=forms.RadioSelect)
    arquero = forms.IntegerField(widget=forms.HiddenInput())
