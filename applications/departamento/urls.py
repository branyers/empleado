from django.contrib import admin
from django.urls import path


def pruebaurl(self):
    print("ruta")


urlpatterns = [
    path('', pruebaurl),
]
