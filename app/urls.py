# -*- coding: utf-8 -*-
from django.urls import path

from . import views


urlpatterns = [
    path('', views.EquipoView.as_view()),
    path('resultado/', views.ResultadoView.as_view()),
]
