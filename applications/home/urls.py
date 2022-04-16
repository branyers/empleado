from django.contrib import admin
from django.urls import path
from .views import (
    pruebaview,
    lista,
    CreatePrueba,
    ListarPrueba
)


urlpatterns = [
    path('prueba', pruebaview.as_view()),
    path('', lista.as_view()),
    path('lista/', ListarPrueba.as_view()),
    path('add/', CreatePrueba.as_view())

]
