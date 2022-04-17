from django.contrib import admin
from django.urls import path
from .views import All_Empleados, All_Empleados_by_Department


urlpatterns = [
    path('List_employees', All_Empleados.as_view()),
    path('by_area/', All_Empleados_by_Department.as_view()),

]
