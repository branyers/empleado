from django.contrib import admin
from django.urls import path

from .views import DepartamentoView


urlpatterns = [
    path('add_departamento/', DepartamentoView.as_view(), name='add_departamento'),
]
