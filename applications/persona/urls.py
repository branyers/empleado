from django.contrib import admin
from django.urls import path
from .views import (

    All_Empleados,
    All_Empleados_by_Department,
    All_empleados_by_Jobs,
    Emplados_por_habilidades,
    Empleados_Detalles,
    Empleados_CreateView,
    successTemplateView,
    Empleado_UpdateView,
    Empleados_Delete,
    Listar_Empleados_Admin,
)

app_name = 'Empleados_app'

urlpatterns = [
    path('List_employees/', All_Empleados.as_view(), name="all_empleados"),
    path('by_area/<name>/', All_Empleados_by_Department.as_view(), name="empleados_by_area"),
    path('by_jobs/', All_empleados_by_Jobs.as_view(), name="empleados_by_jobs"),
    path('by_habilidades/', Emplados_por_habilidades.as_view(), name="emplados_by_habilidades"),
    path('empleados_details/<pk>/', Empleados_Detalles.as_view(), name="empleados_details"),
    path('empleados_create/', Empleados_CreateView.as_view(), name="empleados_create"),
    path('success/', successTemplateView.as_view(), name='success'),
    path('empleado_update/<pk>/', Empleado_UpdateView.as_view(), name='empleado_update'),
    path('empleado_delete/<pk>/', Empleados_Delete.as_view(), name='empleado_delete'),
    path('empleados_admin/', Listar_Empleados_Admin.as_view(), name='empleados_admin'),


]
