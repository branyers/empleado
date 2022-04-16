from pyexpat import model

from django.shortcuts import render
from django.views.generic import ListView

from .models import Persona
# Create your views here.


class All_Empleados(ListView):
    template_name = "usuario/all_empleados.html"
    model = Persona
    context_object_name = 'Empleados_list'


class All_Empleados_by_Department(ListView):
    template_name = "usuario/employees_by_department.html"

    def get_queryset(self):
        area = self.kwargs['name']
        lista = Persona.objects.filter(departament__name=area)
        return lista
    context_object_name = 'empleados'

