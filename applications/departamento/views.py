from django.views.generic.edit import FormView
from .forms import DepartamentoFormView
from applications.persona.models import Persona
from .models import Departamento
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)

class DepartamentoView(FormView):
    template_name = 'departamento/add_departamento.html'
    form_class = DepartamentoFormView
    success_url = '/'

    def form_valid(self,form):

        nombre = form.cleaned_data['Nombre']
        apellido = form.cleaned_data['apellido']
        cargos = form.cleaned_data['cargos']

        Persona.objects.create(
            FirstName=nombre,
            LastName=apellido,
            Jobs=cargos,
            full_name=nombre + " " + apellido,
            departament=Departamento.objects.create(
            name=form.cleaned_data['departamento'],
            short_name=form.cleaned_data['short_name']
        )
    )
        return super(DepartamentoView, self).form_valid(form)


class List_DepartamentoView(ListView):
    template_name = "departamento/all_departamentos.html"
    paginate_by = 4
    model = Departamento
    context_object_name = 'departamentos'

    def get_queryset(self):
        palabraClave = self.request.GET.get('kword','')
        lista = Departamento.objects.filter(name__icontains=palabraClave)
        return lista