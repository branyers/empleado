from rest_framework import routers
from rest_framework.routers import DefaultRouter
from applications.departamento.API.views import DepartamentoViewSet

routers = DefaultRouter()
"""With this router we can handle the urls in the API in specific applications"""
""""With Register we can register using the prefix, basename and ViewSet created in the applications views"""

routers.register(prefix='departamento', basename='departamento', viewset=DepartamentoViewSet)


