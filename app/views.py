# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import TemplateView

from .forms import EquipoForm
from .models import Jugador


class EquipoView(TemplateView):
    template_name = 'app/equipo.html'

    def get_context_data(self, *args, **kwargs):
        context = super(EquipoView, self).get_context_data(*args, **kwargs)
        context['form'] = EquipoForm()
        return context

    def post(self, request, *args, **kwargs):
        form = EquipoForm(request.POST)
        if form.is_valid():
            # Extraemos la informacion solo los campos que nos interesan
            resultado = 0
            ids = [v for k, v in form.cleaned_data.items() if k not in ['jugadores', 'selecciones', 'posiciones']]
            jugadores = Jugador.objects.filter(id__in=ids)
            for jugador in jugadores:
                print(jugador.puntaje)
                resultado += jugador.puntaje
        return reverse('resultado', kwargs={'puntaje': resultado})


class ResultadoView(TemplateView):
    template_name = 'app/resultado.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ResultadoView, self).get_context_data(*args, **kwargs)
        return context
