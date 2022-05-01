

from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)
from .models import Persona
# Create your views here.
from .forms import EmpleadosForm

class InicioView(TemplateView):
    template_name = 'inicio.html'


class All_Empleados(ListView):
    template_name = "usuario/all_empleados.html"
    model = Persona
    context_object_name = 'Empleados_list'
    paginate_by = 4

    def get_queryset(self):
        palabraClave = self.request.GET.get('kword', '')
        lista = Persona.objects.filter(FirstName__icontains=palabraClave)
        return lista


class All_Empleados_by_Department(ListView):
    template_name = "usuario/employees_by_department.html"
    paginate_by = 4

    """Form to do a statement for a search box"""
    # def get_queryset(self):
    #     area = self.kwargs['name']
    #     lista = Persona.objects.filter(departament__name=area)
    #     return lista

    """Form to do a statement with a search for a bar search using the method GET"""
    def get_queryset(self):
        area = self.kwargs['name']
        empleado = self.request.GET.get('kword', '')
        lista = Persona.objects.filter(departament__name__icontains=area, FirstName__icontains=empleado)
        return lista
    context_object_name = 'empleados'
    
    """I used that method for send extra data the template (I am going to continue learn more about this method """
    # def get_context_data(self, **kwargs):
    #     context = super(All_Empleados_by_Department, self).get_context_data(**kwargs)
    #     context['area'] = self.request.GET.get('kword', '')
    #     return context


class All_empleados_by_Jobs(ListView):
    template_name = "usuario/employees_by_jobs.html"
    paginate_by = 3

    def get_queryset(self):
        jobs = self.request.GET.get('kword','')
        lista = Persona.objects.filter(Jobs=jobs)
        return lista


class Listar_Empleados_Admin(ListView):
    template_name = 'usuario/listar_empeados.html'
    ordering = 'FirstName'
    model = Persona
    paginate_by = 10

    def get_queryset(self):
        empleado = self.request.GET.get('kword', '')
        lista = Persona.objects.filter(FirstName__icontains=empleado)
        return lista

    context_object_name = 'empleados'


class Emplados_por_habilidades(ListView):
    template_name = "usuario/empleados_por_habilidades.html"

    def get_queryset(self):
        id_Empleado = self.request.GET.get('kword', '')
        list = Persona.objects.get(id=id_Empleado)
        habilidades = list.habilidades.all()
        return habilidades

    context_object_name = 'empleados'


class Empleados_Detalles(DetailView):
    template_name = 'usuario/empleados_details.html'
    model = Persona
    context_object_name = 'empleados'


class successTemplateView(TemplateView):
    template_name = 'usuario/success.html'


class Empleados_CreateView(CreateView):
    template_name = 'usuario/create_empleados.html'
    model = Persona
    """For get all attributes of model"""
    # fields = ('__all__')
    form_class = EmpleadosForm

    # fields = (
    #     'FirstName',
    #     'LastName',
    #     'Jobs',
    #     'departament',
    #     'avatar',
    #     'habilidades',
    # )
    success_url = reverse_lazy('Empleados_app:empleados_admin')

    """This function is for validate the data before been save in the database and add extra data in case that were possible"""
    # def form_valid(self, form):
    #     empleado = form.save(commit=False)
    #     empleado.full_name = empleado.FirstName + " " + empleado.LastName
    #     empleado.save()
    #     return super(Empleados_CreateView, self).form_valid(form)


class Empleado_UpdateView(UpdateView):
    template_name = "usuario/empleado_update.html"
    model = Persona
    fields = [
        'FirstName',
        'LastName',
        'Jobs',
        'habilidades',
        'departament',
        'avatar'
    ]

    success_url = reverse_lazy("Empleados_app:empleados_admin")


class Empleados_Delete(DeleteView):
    template_name = "usuario/eliminar_empleados.html"
    model = Persona
    context_object_name = "empleado"
    success_url = reverse_lazy("Empleados_app:empleados_admin")





