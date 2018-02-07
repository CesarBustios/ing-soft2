# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import TemplateView


class EquipoView(TemplateView):
    template_name = 'app/equipo.html'

    def get_context_data(self, *args, **kwargs):
        context = super(EquipoView, self).get_context_data(*args, **kwargs)
        return context


class ResultadoView(TemplateView):
    template_name = 'app/resultado.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ResultadoView, self).get_context_data(*args, **kwargs)
        return context
