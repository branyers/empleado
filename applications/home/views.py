from .models import Prueba
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView

)

from .forms import PruebaForm


# Create your views here.

class pruebaview(TemplateView):
    template_name = 'home/home.html'


class lista(ListView):
    template_name = "home/lista.html"
    context_object_name = "lista"
    queryset = [0,1,2,3,4,4,5]


class ListarPrueba(ListView):
    template_name = 'home/prueba_listar.html'
    model = Prueba
    context_object_name = 'lista_prueba'


class CreatePrueba(CreateView):
    template_name = 'home/add.html'
    model = Prueba
    form_class = PruebaForm
    success_url = "/"



