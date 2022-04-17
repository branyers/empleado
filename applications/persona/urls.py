from django.contrib import admin
from django.urls import path
from .views import All_Empleados, All_Empleados_by_Department, All_empleados_by_Jobs, Emplados_por_habilidades


urlpatterns = [
    path('List_employees', All_Empleados.as_view()),
    path('by_area/', All_Empleados_by_Department.as_view()),
    path('by_jobs/', All_empleados_by_Jobs.as_view()),
    path('by_habilidades/', Emplados_por_habilidades.as_view()),


]
