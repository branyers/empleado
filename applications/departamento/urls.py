from django.contrib import admin
from django.urls import path

from .views import DepartamentoView, List_DepartamentoView

app_name = 'Departamento_app'

urlpatterns = [
    path('add_departamento/', DepartamentoView.as_view(), name='add_departamento'),
    path('list_departamentos/', List_DepartamentoView.as_view(), name='list_departamentos'),

]
