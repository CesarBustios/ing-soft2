# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import TemplateView

from .forms import EquipoForm


class EquipoView(TemplateView):
    template_name = 'app/equipo.html'

    def get_context_data(self, *args, **kwargs):
        context = super(EquipoView, self).get_context_data(*args, **kwargs)
        context['form'] = EquipoForm()
        return context


class ResultadoView(TemplateView):
    template_name = 'app/resultado.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ResultadoView, self).get_context_data(*args, **kwargs)
        return context
