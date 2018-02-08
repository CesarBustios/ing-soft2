# -*- coding: utf-8 -*-
from django import forms

from .models import Seleccion, Jugador


class EquipoForm(forms.Form):
    POSICIONES_CHOICES = (
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
    posiciones = forms.ChoiceField(choices=POSICIONES_CHOICES, widget=forms.RadioSelect)
    arquero = forms.IntegerField(widget=forms.HiddenInput())
    defensa1 = forms.IntegerField(widget=forms.HiddenInput())
    defensa2 = forms.IntegerField(widget=forms.HiddenInput())
    defensa3 = forms.IntegerField(widget=forms.HiddenInput())
    defensa4 = forms.IntegerField(widget=forms.HiddenInput())
    centro1 = forms.IntegerField(widget=forms.HiddenInput())
    centro2 = forms.IntegerField(widget=forms.HiddenInput())
    centro3 = forms.IntegerField(widget=forms.HiddenInput())
    delantero1 = forms.IntegerField(widget=forms.HiddenInput())
    delantero2 = forms.IntegerField(widget=forms.HiddenInput())
    delantero3 = forms.IntegerField(widget=forms.HiddenInput())
    selecciones = forms.ModelChoiceField(queryset=Seleccion.objects.all().order_by('pais'))
    jugadores = forms.ModelChoiceField(queryset=Jugador.objects.all().order_by('nombre'))

    def __init__(self, *args, **kwargs):
        super(EquipoForm, self).__init__(*args, **kwargs)
        self.fields['selecciones'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['jugadores'].widget.attrs = {
            'class': 'form-control'
        }
